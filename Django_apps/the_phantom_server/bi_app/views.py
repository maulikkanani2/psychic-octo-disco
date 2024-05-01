from io import BytesIO
from datetime import timedelta, datetime
import csv, os
import uuid
import requests
from bokeh.embed import components
from bokeh.models import CheckboxGroup, Select
from xhtml2pdf import pisa
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from django.db.models import Sum, DateField
from django.db.models.functions import Trunc
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from django.db import connections
from django.http import (
    HttpResponseRedirect,
    HttpResponseBadRequest,
)
from the_phantom_server.utils import (
    calculate_average,
    create_alias_queryset,
    double_line_regular_chart,
    single_line_date_chart,
    single_line_date_chart_day,
)


from .filters import OilLedgerFilter, FlowControllerDataFilter
from .models import (
    Docgasmeterreadings,
    OilLedger,
    Doccompressors,
    Docruntickets,
    Docwaterdisposition,
    Docwelltests,
    modem,
    device,
    Tag,
    flow_controller_data,
    Sumdailyproduction,
    Ptsproductionpt,
    Device_inputs,
)
from .forms import (
    GasMeterForm,
    DocCompressorsForm,
    DocrunticketsForm,
    DocwaterdispositionForm,
    DocwelltestsForm,
    ModemForm,
    TagForm,
    DeviceForm,
    DeviceInputForm,
)
import logging

import holoviews as hv
import geoviz, holoviews
import geoviews as gv
from zip_file_script.zip_script import SHP_DATA, ReadSHP
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString, MultiLineString
import geoviews.feature as gf
from geoviews import opts
from cartopy import crs
from bokeh.models import HoverTool

logger = logging.getLogger(__name__)


# from API.views import create_tag as create_tag_api, create_modem as modem_api
def generate_unique_value():
    """
    Generates a unique value for the docidcompressors field.
    You can customize this function based on your requirements.
    """
    uuid_value = uuid.uuid4()
    uuid_int = int(uuid_value.int) % (10**7)
    return uuid_int


def home(request):
    return render(request, "home.html")


# def home(request):
#     return render(request, status=500)
# def create_tag(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             # Instead of saving the form directly, we'll pass the data to the API endpoint
#             response = create_tag_api(request)
#             if response.status_code == 201:  # Assuming 201 indicates successful creation
#                 return redirect('tag_list')  # Redirect to the tag list view after successful creation
#             else:
#                 # Handle error case, maybe display error message to the user
#                 pass
#     else:
#         form = TagForm()
#     return render(request, 'tag_form.html', {'form': form})


def pdf(request):
    try:
        # Default to "2023-10-01" if 'docdatedate' is not provided in the GET request
        selected_date_str = request.GET.get("docdatedate", "2023-10-01")

        # Convert the selected date to a datetime object
        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
        except ValueError:
            return HttpResponseBadRequest(
                "Invalid format for docdatedate. Please use 'YYYY-MM-DD'."
            )

        sixty_days_ago = selected_date - timedelta(days=60)

        try:
            oil = OilLedger.objects.filter(
                docdatedate__range=[sixty_days_ago, datetime.now()]
            )
            oil = oil.select_related("tankid__cal_id", "tankid__tankname")
        except Exception as e:
            oil = OilLedger.objects.none()

        cols = [
            "tankid__cal_id__name",
            "tankid__tankname",
            "final_gauge",
            "docdatedate",
            "rtvolume",
            "production",
        ]
        alias_cols = ["Location", "Tank_name", "Volume", "Date", "Sales", "Production"]
        annotated_oil = create_alias_queryset(oil.values(*cols), alias_cols, cols)

        filter_params = {"docdatedate": selected_date_str}
        oil_ledger_filter = OilLedgerFilter(filter_params, queryset=annotated_oil)

        context = {
            "oil": oil_ledger_filter.qs,
        }

        return render(request, "exports/pdf.html", context)
    except Exception as e:
        return HttpResponse(str(e))


@login_required
def consolidated_production(request):
    context = {}
    try:
        ptsproductionpt = Ptsproductionpt.objects.all().order_by("productionptid")
        if not ptsproductionpt:
            raise Http404("No Ptsproductionpt objects found.")
        initial_ptsproductionptid = ptsproductionpt.first().productionptid
        productionptid = request.GET.get("ptrid", initial_ptsproductionptid)
        sumdailyproduction = Sumdailyproduction.objects.filter(
            entityid__productionptid=productionptid
        )
        data_line_chart1 = {
            "x_values": [1, 2, 3, 4, 5],
            "y_values": [10, 8, 6, 4, 2],
            "y2_values": [8, 12, 16, 24, 32],
        }

        data_line_chart2 = {
            "x_values": [1, 2, 3, 4, 5],
            "y_values": [10, 8, 6, 4, 2],
            "y2_values": [8, 12, 16, 24, 32],
        }

        line_chart1 = double_line_regular_chart(data_line_chart1)
        line_chart2 = double_line_regular_chart(data_line_chart2)

        # Embed the charts in the HTML template
        script_line_chart1, div_line_chart1 = components(line_chart1)
        popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)
        script_line_chart2, div_line_chart2 = components(line_chart2)
        popup_script_line_chart2, popup_div_line_chart2 = components(line_chart2)

        context = {
            "script_line_chart1": script_line_chart1,
            "div_line_chart1": div_line_chart1,
            "script_line_chart2": script_line_chart2,
            "div_line_chart2": div_line_chart2,
            "popup_script_line_chart1": popup_script_line_chart1,
            "popup_div_line_chart1": popup_div_line_chart1,
            "popup_script_line_chart2": popup_script_line_chart2,
            "popup_div_line_chart2": popup_div_line_chart2,
            "ptsproductionpt": ptsproductionpt,
            "sumdailyproduction": sumdailyproduction,
            "productionptid": productionptid,
            "is_error": False,
        }
    except Http404 as e:
        context["is_error"] = True
        context["error"] = str(e)
    except Exception as e:
        context["is_error"] = True
        context["error"] = str(e)
    return render(request, "consolidated_production.html", context)


@login_required
def well_analysis(request):
    context = {}
    try:
        # Data for the charts (replace with your actual data)
        ptsproductionpt = Ptsproductionpt.objects.all()
        if not ptsproductionpt:
            raise Http404("No Ptsproductionpt objects found.")
        productionptid = request.GET.get("well_view", None)
        sumdailyproduction = Sumdailyproduction.objects.filter(
            entityid__productionptid=productionptid
        )

        data_line_chart1 = {
            "x_values": [1, 2, 3, 4, 5],
            "y_values": [10, 8, 6, 4, 2],
            "y2_values": [8, 12, 16, 24, 32],
        }

        data_line_chart2 = {
            "x_values": [1, 2, 3, 4, 5],
            "y_values": [10, 8, 6, 4, 2],
            "y2_values": [8, 12, 16, 24, 32],
        }

        data_line_chart3 = {
            "x_values": [1, 2, 3, 4, 5],
            "y_values": [10, 8, 6, 4, 2],
            "y2_values": [8, 12, 16, 24, 32],
        }

        # Create Bokeh charts
        line_chart1 = double_line_regular_chart(data_line_chart1)
        line_chart2 = double_line_regular_chart(data_line_chart2)
        line_chart3 = double_line_regular_chart(data_line_chart3)

        # Embed the charts in the HTML template
        script_line_chart1, div_line_chart1 = components(line_chart1)
        script_line_chart2, div_line_chart2 = components(line_chart2)
        script_line_chart3, div_line_chart3 = components(line_chart3)
        popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)
        popup_script_line_chart2, popup_div_line_chart2 = components(line_chart2)
        popup_script_line_chart3, popup_div_line_chart3 = components(line_chart3)

        context = {
            "script_line_chart1": script_line_chart1,
            "div_line_chart1": div_line_chart1,
            "script_line_chart2": script_line_chart2,
            "div_line_chart2": div_line_chart2,
            "script_line_chart3": script_line_chart3,
            "div_line_chart3": div_line_chart3,
            "popup_script_line_chart1": popup_script_line_chart1,
            "popup_script_line_chart2": popup_script_line_chart2,
            "popup_script_line_chart3": popup_script_line_chart3,
            "popup_div_line_chart1": popup_div_line_chart1,
            "popup_div_line_chart2": popup_div_line_chart2,
            "popup_div_line_chart3": popup_div_line_chart3,
            "ptsproductionpt": ptsproductionpt,
            "sumdailyproduction": sumdailyproduction,
            "productionptid": productionptid,
            "is_error": False,
        }
    except Http404 as e:
        context["is_error"] = True
        context["error"] = str(e)
    except Exception as e:
        context["is_error"] = True
        context["error"] = str(e)
    return render(request, "well_analytics.html", context)


@login_required
def realtime(request):
    return render(request, "realtime_production.html")


@login_required
def oil_inventory(request):
    try:
        # Default to "2023-10-01" if 'docdatedate' is not provided in the GET request
        selected_date_str = request.GET.get("docdatedate", "2023-10-01")

        # Convert the selected date to a datetime object
        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
        except ValueError:
            return HttpResponseBadRequest(
                "Invalid format for docdatedate. Please use 'YYYY-MM-DD'."
            )

        # Get the date 60 days before the selected date
        sixty_days_ago = selected_date - timedelta(days=60)

        # query OilLedger objects within the last 60 days
        try:
            oil = OilLedger.objects.filter(
                docdatedate__range=[sixty_days_ago, datetime.now()]
            )
            oil = oil.select_related("tankid__cal_id", "tankid__tankname")
        except Exception as e:
            oil = OilLedger.objects.none()

        cols = [
            "tankid__cal_id__name",
            "tankid__tankname",
            "final_gauge",
            "docdatedate",
            "rtvolume",
            "production",
        ]
        alias_cols = ["Location", "Tank_name", "Volume", "Date", "Sales", "Production"]
        # take the oil query and create an annotated query
        annotated_oil = create_alias_queryset(oil.values(*cols), alias_cols, cols)

        daily_totals = (
            annotated_oil.values(
                "docdatedate"
            )  # the subsequent aggregation will be performed for each unique value of docdatedate.
            .annotate(
                total_sales=Sum("Sales"),
                total_volume=Sum("Volume"),
                total_production=Sum("Production"),
            )
            .order_by("docdatedate")
        )
        filter_params = {"docdatedate": selected_date_str}
        # use custom filter oilledgerfilter to get a daily ledger by well
        oil_ledger_filter = OilLedgerFilter(filter_params, queryset=annotated_oil)

        if daily_totals.exists():
            volume_chart = single_line_date_chart_day(
                data=daily_totals,
                x_column="docdatedate",
                y_column="total_volume",
                y_axis_label="BBls",
                x_axis_label="Date",
                legend_label="Volume",
            )
            sales_chart = single_line_date_chart_day(
                data=daily_totals,
                x_column="docdatedate",
                y_column="total_sales",
                y_axis_label="BBls",
                x_axis_label="Date",
                legend_label="Volume",
            )
            Production_chart = single_line_date_chart_day(
                data=daily_totals,
                x_column="docdatedate",
                y_column="total_production",
                y_axis_label="BBls",
                x_axis_label="Date",
                legend_label="Volume",
            )

            script_line_chart1, div_line_chart1 = components(volume_chart)
            script_line_chart2, div_line_chart2 = components(sales_chart)
            script_line_chart3, div_line_chart3 = components(Production_chart)
            popup_script_line_chart1, popup_div_line_chart1 = components(volume_chart)
            popup_script_line_chart2, popup_div_line_chart2 = components(sales_chart)
            popup_script_line_chart3, popup_div_line_chart3 = components(
                Production_chart
            )

            average_sales = calculate_average(daily_totals, "total_sales")
            average_production = calculate_average(daily_totals, "total_production")
            average_inventory = calculate_average(daily_totals, "total_volume")
        else:
            # Default Values
            average_sales = None
            average_production = None
            average_inventory = None
            script_line_chart1 = None
            div_line_chart1 = None
            script_line_chart2 = None
            div_line_chart2 = None
            script_line_chart3 = None
            div_line_chart3 = None

            popup_script_line_chart1 = None
            popup_div_line_chart1 = None
            popup_script_line_chart2 = None
            popup_div_line_chart2 = None
            popup_script_line_chart3 = None
            popup_div_line_chart3 = None

        context = {
            "form": oil_ledger_filter.form,
            "oil": oil_ledger_filter.qs,
            "sixty_days_data": daily_totals,
            "average_sales": average_sales,
            "average_production": average_production,
            "average_inventory": average_inventory,
            "script_line_chart1": script_line_chart1,
            "div_line_chart1": div_line_chart1,
            "script_line_chart2": script_line_chart2,
            "div_line_chart2": div_line_chart2,
            "script_line_chart3": script_line_chart3,
            "div_line_chart3": div_line_chart3,
            "popup_script_line_chart1": popup_script_line_chart1,
            "popup_script_line_chart2": popup_script_line_chart2,
            "popup_script_line_chart3": popup_script_line_chart3,
            "popup_div_line_chart1": popup_div_line_chart1,
            "popup_div_line_chart2": popup_div_line_chart2,
            "popup_div_line_chart3": popup_div_line_chart3,
        }

        return render(request, "Oil_Inventory.html", context)

    except Exception as e:
        # return HttpResponseServerError(str(e))
        return render(request, "error_404.html", {"context": str(e)})


@login_required
def wellhead_automation(request):
    try:
        # Default to "2023-10-01" if 'timestamp' is not provided in the GET request
        selected_date_str = request.GET.get("timestamp", "2024-02-23")

        # Convert the selected date to a datetime object
        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
        except ValueError:
            return HttpResponseBadRequest(
                "Invalid format for timestamp. Please use 'YYYY-MM-DD'."
            )

        # Get the date 60 days before the selected date
        sixty_days_ago = selected_date - timedelta(days=60)

        # query flow_controller_data objects within the last 60 days
        try:
            well_head = flow_controller_data.objects.filter(
                timestamp__range=[sixty_days_ago, datetime.now()]
            )
            well_head = well_head.select_related("device")
        except Exception as e:
            well_head = flow_controller_data.objects.none()

        cols = [
            "device__device_name",
            "current_output",
            "line_pressure",
            "well_pressure",
            "last_action",
            "timestamp",
        ]
        alias_cols = [
            "Name",
            "Opening",
            "Line_Pressure",
            "Well_presure",
            "Last_action",
            "Date",
        ]
        annotated_well_head = create_alias_queryset(
            well_head.values(*cols), alias_cols, cols
        )

        daily_totals = (
            annotated_well_head.values("timestamp")
            .annotate(
                line_pressure=Sum("Line_Pressure"),
                well_pressure=Sum("Well_presure"),
                current_output=Sum("current_output"),
                truncated_date=Trunc("timestamp", "day", output_field=DateField()),
            )
            .order_by("timestamp")
        )

        filter_params = {"timestamp": selected_date}
        well_head_ledger_filter = FlowControllerDataFilter(
            data=filter_params, queryset=annotated_well_head
        )

        if daily_totals.exists():
            line_pressure_chart = single_line_date_chart_day(
                data=daily_totals,
                x_column="timestamp",
                y_column="line_pressure",
                y_axis_label="BBls",
                x_axis_label="truncated_date",
                legend_label="Volume",
            )
            well_presure_chart = single_line_date_chart_day(
                data=daily_totals,
                x_column="timestamp",
                y_column="well_pressure",
                y_axis_label="BBls",
                x_axis_label="truncated_date",
                legend_label="Volume",
            )

            script_line_chart1, div_line_chart1 = components(line_pressure_chart)
            script_line_chart2, div_line_chart2 = components(well_presure_chart)
            popup_script_line_chart1, popup_div_line_chart1 = components(
                line_pressure_chart
            )
            popup_script_line_chart2, popup_div_line_chart2 = components(
                well_presure_chart
            )

            average_line_pressure = calculate_average(daily_totals, "line_pressure")
            average_well_pressure = calculate_average(daily_totals, "well_pressure")
        else:
            # Default Values
            average_line_pressure = None
            average_well_pressure = None
            script_line_chart1 = None
            div_line_chart1 = None
            script_line_chart2 = None
            div_line_chart2 = None

            popup_script_line_chart1 = None
            popup_div_line_chart1 = None
            popup_script_line_chart2 = None
            popup_div_line_chart2 = None

        context = {
            "form": well_head_ledger_filter.form,
            "well_head": well_head_ledger_filter.qs,
            "sixty_days_data": daily_totals,
            "average_line_pressure": average_line_pressure,
            "average_well_pressure": average_well_pressure,
            "script_line_chart1": script_line_chart1,
            "div_line_chart1": div_line_chart1,
            "script_line_chart2": script_line_chart2,
            "div_line_chart2": div_line_chart2,
            "popup_script_line_chart1": popup_script_line_chart1,
            "popup_script_line_chart2": popup_script_line_chart2,
            "popup_div_line_chart1": popup_div_line_chart1,
            "popup_div_line_chart2": popup_div_line_chart2,
        }

        return render(request, "wellhead_automation.html", context)

    except Exception as e:
        # return HttpResponseServerError(str(e))
        return render(request, "error_404.html", {"context": str(e)})


@login_required
def reserves(request):
    # Data for the charts (replace with your actual data)
    data_line_chart1 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart2 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart3 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    # Create Bokeh charts
    line_chart1 = double_line_regular_chart(data_line_chart1)
    line_chart2 = double_line_regular_chart(data_line_chart2)
    line_chart3 = double_line_regular_chart(data_line_chart3)

    # Embed the charts in the HTML template
    script_line_chart1, div_line_chart1 = components(line_chart1)
    script_line_chart2, div_line_chart2 = components(line_chart2)
    script_line_chart3, div_line_chart3 = components(line_chart3)
    popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)
    popup_script_line_chart2, popup_div_line_chart2 = components(line_chart2)
    popup_script_line_chart3, popup_div_line_chart3 = components(line_chart3)

    context = {
        "script_line_chart1": script_line_chart1,
        "div_line_chart1": div_line_chart1,
        "script_line_chart2": script_line_chart2,
        "div_line_chart2": div_line_chart2,
        "script_line_chart3": script_line_chart3,
        "div_line_chart3": div_line_chart3,
        "popup_script_line_chart1": popup_script_line_chart1,
        "popup_script_line_chart2": popup_script_line_chart2,
        "popup_script_line_chart3": popup_script_line_chart3,
        "popup_div_line_chart1": popup_div_line_chart1,
        "popup_div_line_chart2": popup_div_line_chart2,
        "popup_div_line_chart3": popup_div_line_chart3,
    }
    return render(request, "reserves.html", context)


@login_required
def injection(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Data for the charts (replace with your actual data)
    data_line_chart1 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart2 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart3 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    # Create Bokeh charts
    line_chart1 = double_line_regular_chart(data_line_chart1)
    line_chart2 = double_line_regular_chart(data_line_chart2)
    line_chart3 = double_line_regular_chart(data_line_chart3)

    # Embed the charts in the HTML template
    script_line_chart1, div_line_chart1 = components(line_chart1)
    script_line_chart2, div_line_chart2 = components(line_chart2)
    script_line_chart3, div_line_chart3 = components(line_chart3)
    popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)
    popup_script_line_chart2, popup_div_line_chart2 = components(line_chart2)
    popup_script_line_chart3, popup_div_line_chart3 = components(line_chart3)

    context = {
        "script_line_chart1": script_line_chart1,
        "div_line_chart1": div_line_chart1,
        "script_line_chart2": script_line_chart2,
        "div_line_chart2": div_line_chart2,
        "script_line_chart3": script_line_chart3,
        "div_line_chart3": div_line_chart3,
        "popup_script_line_chart1": popup_script_line_chart1,
        "popup_script_line_chart2": popup_script_line_chart2,
        "popup_script_line_chart3": popup_script_line_chart3,
        "popup_div_line_chart1": popup_div_line_chart1,
        "popup_div_line_chart2": popup_div_line_chart2,
        "popup_div_line_chart3": popup_div_line_chart3,
    }
    return render(request, "injection.html", context)


@login_required
def production_analysis(request):
    # Data for the charts (replace with your actual data)
    data_line_chart1 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart2 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    data_line_chart3 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    checkbox_labels = ["Line 1", "Line 2"]
    checkbox_group = CheckboxGroup(labels=checkbox_labels, active=[0, 1])
    # Create Bokeh charts
    line_chart1 = double_line_regular_chart(data_line_chart1)
    line_chart2 = double_line_regular_chart(data_line_chart2)
    line_chart3 = double_line_regular_chart(data_line_chart3)

    # Create Select widgets
    select1 = Select(
        title="Select Option 1",
        value="Option 1",
        options=["Option 1", "Option 2", "Option 3"],
    )
    select2 = Select(
        title="Select Option 2",
        value="Option 1",
        options=["Option 1", "Option 2", "Option 3"],
    )
    select3 = Select(
        title="Select Option 3",
        value="Option 1",
        options=["Option 1", "Option 2", "Option 3"],
    )
    select4 = Select(
        title="Select Option 4",
        value="Option 1",
        options=["Option 1", "Option 2", "Option 3"],
    )

    # Embed the charts in the HTML template
    script_line_chart1, div_line_chart1 = components(line_chart1)
    script_line_chart2, div_line_chart2 = components(line_chart2)
    script_line_chart3, div_line_chart3 = components(line_chart3)
    popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)
    popup_script_line_chart2, popup_div_line_chart2 = components(line_chart2)
    popup_script_line_chart3, popup_div_line_chart3 = components(line_chart3)

    return render(
        request,
        "production_analysis.html",
        {
            "script_line_chart1": script_line_chart1,
            "div_line_chart1": div_line_chart1,
            "checkbox_group": checkbox_group,
            "script_line_chart2": script_line_chart2,
            "div_line_chart2": div_line_chart2,
            "script_line_chart3": script_line_chart3,
            "div_line_chart3": div_line_chart3,
            "select1": select1,
            "select2": select2,
            "select3": select3,
            "select4": select4,
            "popup_script_line_chart1": popup_script_line_chart1,
            "popup_script_line_chart2": popup_script_line_chart2,
            "popup_script_line_chart3": popup_script_line_chart3,
            "popup_div_line_chart1": popup_div_line_chart1,
            "popup_div_line_chart2": popup_div_line_chart2,
            "popup_div_line_chart3": popup_div_line_chart3,
        },
    )


@login_required
def all_gas(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    gas_list = Docgasmeterreadings.objects.order_by("-docdate")[:10]
    # Docgasmeterreadings.objects.all()
    return render(request, "gas_meter_view.html", {"gas_list": gas_list})


@login_required
def gas_meter(request):
    """
    View for handling gas meter readings.
    GET requests render a blank form, and POST requests process the form.
    Additionally, fetches the last 10 records for display.
    """
    errors = None
    submitted = False
    form = GasMeterForm()
    try:
        # Fetch the latest 10 records for display
        latest_records = Docgasmeterreadings.objects.order_by("-docdate")[:10]

        # Check if the form was previously submitted
        if request.method == "POST":
            form = GasMeterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(
                    reverse("gas_meter_input") + "?submitted=True"
                )
            else:
                return render(
                    request,
                    "gas_meter.html",
                    {
                        "form": form,
                        "submitted": submitted,
                        "errors": form.errors,
                        "latest_records": latest_records,
                    },
                )
        else:
            form = GasMeterForm()  # Create a blank form
            if "submitted" in request.GET:
                submitted = True
    except Exception as e:
        print(str(e))
        errors = str(e)

    return render(
        request,
        "gas_meter.html",
        {
            "form": form,
            "submitted": submitted,
            "errors": errors,
            "latest_records": latest_records,
        },
    )


@login_required
def doc_compressors(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    errors = None
    submitted = False
    form = DocCompressorsForm()
    try:
        latest_records = Doccompressors.objects.order_by("-docdate")[:10]

        if request.method == "POST":
            form = DocCompressorsForm(request.POST)
            if form.is_valid():
                form.instance.docidcompressors = generate_unique_value()
                form.save()
                return HttpResponseRedirect(
                    reverse("doc_compressor_input") + "?submitted=True"
                )
            else:
                return render(
                    request,
                    "doc_compressor.html",
                    {
                        "form": form,
                        "submitted": submitted,
                        "errors": form.errors,
                        "latest_records": latest_records,
                    },
                )
        else:
            form = DocCompressorsForm()  # Create a blank form
            if "submitted" in request.GET:
                submitted = True
    except Exception as e:
        print(str(e))
        errors = str(e)
    return render(
        request,
        "doc_compressor.html",
        {
            "form": form,
            "submitted": submitted,
            "errors": errors,
            "latest_records": latest_records,
        },
    )


@login_required
def doc_run_tickets(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    errors = None
    submitted = False
    form = DocrunticketsForm()
    try:
        latest_records = Docruntickets.objects.order_by("-docdate")[:10]

        if request.method == "POST":
            form = DocrunticketsForm(request.POST)
            if form.is_valid():
                form.instance.docidruntickets = generate_unique_value()
                form.save()
                return HttpResponseRedirect(
                    reverse("doc_run_tickets_input") + "?submitted=True"
                )
            else:
                return render(
                    request,
                    "doc_run_tickets.html",
                    {
                        "form": form,
                        "submitted": submitted,
                        "errors": form.errors,
                        "latest_records": latest_records,
                    },
                )
        else:
            form = DocrunticketsForm()  # Create a blank form
            if "submitted" in request.GET:
                submitted = True
    except Exception as e:
        errors = str(e)
        print(str(e))
    return render(
        request,
        "doc_run_tickets.html",
        {
            "form": form,
            "submitted": submitted,
            "errors": errors,
            "latest_records": latest_records,
        },
    )


@login_required
def doc_water_disposition(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    errors = None
    submitted = False
    form = DocwaterdispositionForm()
    try:
        latest_records = Docwaterdisposition.objects.order_by("-docdate")[:10]

        if request.method == "POST":
            form = DocwaterdispositionForm(request.POST)
            if form.is_valid():
                form.instance.docidwaterdisposition = generate_unique_value()
                form.save()
                return HttpResponseRedirect(
                    reverse("doc_water_disposition_input") + "?submitted=True"
                )
            else:
                return render(
                    request,
                    "doc_water_disposition.html",
                    {
                        "form": form,
                        "submitted": submitted,
                        "errors": form.errors,
                        "latest_records": latest_records,
                    },
                )
        else:
            form = DocwaterdispositionForm()  # Create a blank form
            if "submitted" in request.GET:
                submitted = True
    except Exception as e:
        errors = str(e)
        print(str(e))
    return render(
        request,
        "doc_water_disposition.html",
        {
            "form": form,
            "submitted": submitted,
            "errors": errors,
            "latest_records": latest_records,
        },
    )


@login_required
def doc_well_tests(request):
    errors = None
    submitted = False
    form = DocwelltestsForm()
    try:
        latest_records = Docwelltests.objects.order_by("-docdate")[:10]

        if request.method == "POST":
            form = DocwelltestsForm(request.POST)
            if form.is_valid():
                form.instance.docidwelltests = generate_unique_value()
                form.save()
                return HttpResponseRedirect(
                    reverse("doc_well_tests_input") + "?submitted=True"
                )
            else:
                return render(
                    request,
                    "doc_well_tests.html",
                    {
                        "form": form,
                        "submitted": submitted,
                        "errors": form.errors,
                        "latest_records": latest_records,
                    },
                )
        else:
            form = DocwelltestsForm()  # Create a blank form
            if "submitted" in request.GET:
                submitted = True
    except Exception as e:
        errors = str(e)
        print(str(e))
    return render(
        request,
        "doc_well_tests.html",
        {
            "form": form,
            "submitted": submitted,
            "errors": errors,
            "latest_records": latest_records,
        },
    )


"""
def gas_meter(request):
    
    View for handling gas meter readings.
    If recent records exist from the last 10 days, the view will edit the most recent one.
    GET requests render a blank or existing form, and POST requests process the form.
    
    #calculate a form range
    form_range = timezone.now() - timedelta(days=10)
    # Query for recent records
    recent_records = Docgasmeterreadings.objects.filter(docdate__gte=form_range)

    # Get the first recent record if it exists
    instance = recent_records.first() if recent_records.exists() else None

    # Check if the form was previously submitted
    submitted = False
    if request.method == "POST":
        form = GasMeterForm(request.POST, instance=instance)
        if form.is_valid():
            # Save the form if it's valid
            form.save()
            # Redirect to prevent form resubmission
            return HttpResponseRedirect(reverse('gas_meter_input') + '?submitted=True')
        else:
            # Add error handling if form is not valid
            return render(request, 'gas_meter.html', {'form': form, 'submitted': submitted, 'errors': form.errors})
    else:
        form = GasMeterForm(instance=instance)  # Create a form with the instance if it exists
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'gas_meter.html', {'form': form, 'submitted': submitted})
"""


def error_404(request, exception):
    """_summary_

    Args:
        request (_type_): _description_
        exception (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "error_404.html", status=404)


def error_500(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, "error_505.html", status=500)


class Download_data(ViewSet):
    """_summary_

    Args:
        ViewSet (_type_): _description_

    Returns:
        _type_: _description_
    """

    @action(methods=["get"], detail=False, url_path="pdf")
    def download_pdf(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            # Default to "2023-10-01" if 'docdatedate' is not provided in the GET request
            selected_date_str = request.GET.get("docdatedate", "2023-10-01")

            # Convert the selected date to a datetime object
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")

            sixty_days_ago = selected_date - timedelta(days=60)

            try:
                oil = OilLedger.objects.filter(
                    docdatedate__range=[sixty_days_ago, datetime.now()]
                )
                oil = oil.select_related("tankid__cal_id", "tankid__tankname")
            except Exception as e:
                oil = OilLedger.objects.none()

            cols = [
                "tankid__cal_id__name",
                "tankid__tankname",
                "final_gauge",
                "docdatedate",
                "rtvolume",
                "production",
            ]
            alias_cols = [
                "Location",
                "Tank_name",
                "Volume",
                "Date",
                "Sales",
                "Production",
            ]
            annotated_oil = create_alias_queryset(oil.values(*cols), alias_cols, cols)

            filter_params = {"docdatedate": selected_date_str}
            oil_ledger_filter = OilLedgerFilter(filter_params, queryset=annotated_oil)

            if oil_ledger_filter.qs.exists():
                context = {
                    "oil": oil_ledger_filter.qs,
                }

                template = get_template("exports/pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="oil_inventory.pdf"'
                    )
                    return response
            else:
                context = {}
                template = get_template("exports/pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="oil_inventory.pdf"'
                    )
                    return response
        except Exception as e:
            print(str(e))
            context = {}
            template = get_template("exports/pdf.html")
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            if not pdf.err:
                response = HttpResponse(
                    result.getvalue(), content_type="applocation/pdf"
                )
                response["Content-Disposition"] = (
                    'attachment; filename="oil_inventory.pdf"'
                )
                return response
            # return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="csv")
    def download_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            # Default to "2023-10-01" if 'docdatedate' is not provided in the GET request
            selected_date_str = request.GET.get("docdatedate", "2023-10-01")

            # Convert the selected date to a datetime object
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")

            sixty_days_ago = selected_date - timedelta(days=60)

            try:
                oil = OilLedger.objects.filter(
                    docdatedate__range=[sixty_days_ago, datetime.now()]
                )
                oil = oil.select_related("tankid__cal_id", "tankid__tankname")
            except Exception as e:
                oil = OilLedger.objects.none()

            cols = [
                "tankid__cal_id__name",
                "tankid__tankname",
                "final_gauge",
                "docdatedate",
                "rtvolume",
                "production",
            ]
            alias_cols = [
                "Location",
                "Tank_name",
                "Volume",
                "Date",
                "Sales",
                "Production",
            ]
            annotated_oil = create_alias_queryset(oil.values(*cols), alias_cols, cols)

            filter_params = {"docdatedate": selected_date_str}
            oil_ledger_filter = OilLedgerFilter(filter_params, queryset=annotated_oil)

            oil = oil_ledger_filter.qs

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="oil_inventory.csv"'
            writer = csv.writer(response)
            writer.writerow(["Location", "Tank Name", "Current Oil", "Date"])
            if oil.exists():
                for data in oil:
                    writer.writerow(
                        [
                            data["tankid__cal_id__name"],
                            data["tankid__tankname"],
                            data["final_gauge"],
                            data["docdatedate"],
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="gas_meter_pdf")
    def download_gas_meter_pdf(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docgasmeterreadings.objects.order_by("-docdate")[:10]

            if latest_records.exists():
                context = {
                    "latest_records": latest_records,
                }

                template = get_template("exports/gas_meter_pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="gas_meter_pdf.pdf"'
                    )
                    return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="gas_meter_csv")
    def download_gas_meter_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docgasmeterreadings.objects.order_by("-docdate")[:10]

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="gas_meter_csv.csv"'
            writer = csv.writer(response)
            writer.writerow(
                [
                    "Docdate",
                    "Gas meter Readings",
                    "User ID",
                    "Temperature",
                    "Volume",
                    "Line pressure",
                    "Input by Id",
                ]
            )
            if latest_records.exists():
                for data in latest_records:
                    writer.writerow(
                        [
                            data.docdate,
                            data.docidgasmeterreadings,
                            data.userid,
                            data.temperature,
                            data.volume,
                            data.linepressure,
                            data.inputbyid,
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_compressor_pdf")
    def download_doc_compressor_pdf(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Doccompressors.objects.order_by("-docdate")[:10]

            if latest_records.exists():
                context = {
                    "latest_records": latest_records,
                }

                template = get_template("exports/doc_compressor_pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="doc_compressor_pdf.pdf"'
                    )
                    return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_compressor_csv")
    def download_doc_compressor_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Doccompressors.objects.order_by("-docdate")[:10]

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = (
                'attachment; filename="doc_compressor_csv.csv"'
            )
            writer = csv.writer(response)
            writer.writerow(
                [
                    "User ID",
                    "Ambient Temperature",
                    "Discharge Temperature",
                    "Suction Temperature",
                    "Water Temperature",
                    "Oil Pressure",
                    "Oil Temperature",
                    "RPM",
                    "Suction Pressure",
                    "Docdate",
                ]
            )
            if latest_records.exists():
                for data in latest_records:
                    writer.writerow(
                        [
                            data.userid,
                            data.ambienttemp,
                            data.dischargetemperature,
                            data.suctiontemperature,
                            data.watertemp,
                            data.oilpressure,
                            data.oiltemp,
                            data.rpm,
                            data.suctionpressure,
                            data.docdate,
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_run_tickets_pdf")
    def download_doc_run_ticket_pdf(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docruntickets.objects.order_by("-docdate")[:10]

            if latest_records.exists():
                context = {
                    "latest_records": latest_records,
                }

                template = get_template("exports/doc_run_tickets_pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="doc_run_tickets_pdf.pdf"'
                    )
                    return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_run_ticket_csv")
    def download_doc_run_ticket_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docruntickets.objects.order_by("-docdate")[:10]

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = (
                'attachment; filename="doc_run_ticket_csv.csv"'
            )
            writer = csv.writer(response)
            writer.writerow(
                [
                    "Docdate",
                    "End Feet",
                    "End Inch",
                    "End 1/4",
                    "Gravity",
                    "BSW",
                    "Purchaser ID",
                    "Ticket Number",
                    "Volume",
                ]
            )
            if latest_records.exists():
                for data in latest_records:
                    writer.writerow(
                        [
                            data.docdate,
                            data.end_ft,
                            data.end_inch,
                            data.end_qtr,
                            data.gravity,
                            data.bsw,
                            data.purchaserid,
                            data.ticketnum,
                            data.volume,
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_water_disposition_csv")
    def download_doc_water_disposition_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docwaterdisposition.objects.order_by("-docdate")[:10]

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = (
                'attachment; filename="doc_water_disposition_csv.csv"'
            )
            writer = csv.writer(response)
            writer.writerow(
                [
                    "User ID",
                    "Tank ID",
                    "Docdate",
                    "Volume",
                    "Reason Code",
                    "Start Level",
                    "End Level",
                    "On Seal",
                    "Off Seal",
                    "Valve Type ID",
                    "Disposal Site ID",
                    "Transporter ID",
                    "Stamp",
                    "Notes",
                    "Input By ID",
                    "Doc Source Code",
                    "Noru",
                    "New",
                ]
            )
            if latest_records.exists():
                for data in latest_records:
                    writer.writerow(
                        [
                            data.userid,
                            data.tankid,
                            data.docdate,
                            data.volume,
                            data.reasoncode,
                            data.startlevel,
                            data.endlevel,
                            data.onseal,
                            data.offseal,
                            data.valvetypeid,
                            data.disposalsiteid,
                            data.transporterid,
                            data.stamp,
                            data.notes,
                            data.inputbyid,
                            data.docsourcecode,
                            data.noru,
                            data.new,
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="doc_well_tests_csv")
    def download_doc_well_tests_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            latest_records = Docwelltests.objects.order_by("-docdate")[:10]

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = (
                'attachment; filename="doc_well_tests_csv.csv"'
            )
            writer = csv.writer(response)
            writer.writerow(
                [
                    "User ID",
                    "Docdate",
                    "Well Site ID",
                    "Entity ID",
                    "Entity Type ID",
                    "Hourson",
                    "Run Time Perc",
                    "Choke Size",
                    "Not Foral Location",
                    "Test Method",
                    "Oil",
                    "Gas",
                    "Water",
                    "Stamp",
                    "Notes",
                    "Input By ID",
                    "Doc Source Code",
                    "Noru",
                ]
            )
            if latest_records.exists():
                for data in latest_records:
                    writer.writerow(
                        [
                            data.userid,
                            data.docdate,
                            data.wellsiteid,
                            data.entityid,
                            data.entitytypeid,
                            data.hourson,
                            data.runtimeperc,
                            data.chokesize,
                            data.notforallocation,
                            data.testmethod,
                            data.oil,
                            data.gas,
                            data.water,
                            data.stamp,
                            data.notes,
                            data.inputbyid,
                            data.docsourcecode,
                            data.noru,
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="well_head_pdf")
    def download_well_head_pdf(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            # Default to "2023-10-01" if 'timestamp' is not provided in the GET request
            selected_date_str = request.GET.get("timestamp", "2023-10-01")

            # Convert the selected date to a datetime object
            try:
                selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
            except ValueError:
                return HttpResponseBadRequest(
                    "Invalid format for timestamp. Please use 'YYYY-MM-DD'."
                )

            # Get the date 60 days before the selected date
            sixty_days_ago = selected_date - timedelta(days=60)

            # query flow_controller_data objects within the last 60 days
            try:
                well_head = flow_controller_data.objects.filter(
                    timestamp__range=[sixty_days_ago, datetime.now()]
                )
                well_head = well_head.select_related("device")
            except Exception as e:
                well_head = flow_controller_data.objects.none()

            cols = [
                "device__device_name",
                "current_output",
                "line_pressure",
                "well_pressure",
                "last_action",
                "timestamp",
            ]
            alias_cols = [
                "Name",
                "Opening",
                "Line_Pressure",
                "Well_presure",
                "Last_action",
                "Date",
            ]
            annotated_well_head = create_alias_queryset(
                well_head.values(*cols), alias_cols, cols
            )

            filter_params = {"timestamp": selected_date}
            well_head_ledger_filter = FlowControllerDataFilter(
                data=filter_params, queryset=annotated_well_head
            )

            if well_head_ledger_filter.qs.exists():
                context = {
                    "well_head": well_head_ledger_filter.qs,
                }

                template = get_template("exports/well_head_pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="well_head_pdf.pdf"'
                    )
                    return response
            else:
                context = {}
                template = get_template("exports/pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="oil_inventory.pdf"'
                    )
                    return response
        except Exception as e:
            print(str(e))
            context = {}
            template = get_template("exports/pdf.html")
            html = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            if not pdf.err:
                response = HttpResponse(
                    result.getvalue(), content_type="applocation/pdf"
                )
                response["Content-Disposition"] = (
                    'attachment; filename="oil_inventory.pdf"'
                )
                return response

    @action(methods=["get"], detail=False, url_path="well_head_csv")
    def download_well_head_csv(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            # Default to "2023-10-01" if 'timestamp' is not provided in the GET request
            selected_date_str = request.GET.get("timestamp", "2023-10-01")

            # Convert the selected date to a datetime object
            try:
                selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d")
            except ValueError:
                return HttpResponseBadRequest(
                    "Invalid format for timestamp. Please use 'YYYY-MM-DD'."
                )

            # Get the date 60 days before the selected date
            sixty_days_ago = selected_date - timedelta(days=60)

            # query flow_controller_data objects within the last 60 days
            try:
                well_head = flow_controller_data.objects.filter(
                    timestamp__range=[sixty_days_ago, datetime.now()]
                )
                well_head = well_head.select_related("device")
            except Exception as e:
                well_head = flow_controller_data.objects.none()

            cols = [
                "device__device_name",
                "current_output",
                "line_pressure",
                "well_pressure",
                "last_action",
                "timestamp",
            ]
            alias_cols = [
                "Name",
                "Opening",
                "Line_Pressure",
                "Well_presure",
                "Last_action",
                "Date",
            ]
            annotated_well_head = create_alias_queryset(
                well_head.values(*cols), alias_cols, cols
            )

            filter_params = {"timestamp": selected_date}
            well_head_filter = FlowControllerDataFilter(
                data=filter_params, queryset=annotated_well_head
            )

            well_head = well_head_filter.qs

            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="well_head.csv"'
            writer = csv.writer(response)
            writer.writerow(
                [
                    "Device Name",
                    "Current Output",
                    "Line Pressure",
                    "Well Pressure",
                    "Last action",
                ]
            )
            if well_head.exists():
                for data in well_head:
                    writer.writerow(
                        [
                            data["device__device_name"],
                            data["current_output"],
                            data["line_pressure"],
                            data["well_pressure"],
                            data["last_action"],
                        ]
                    )

            return response
        except Exception as e:
            return HttpResponse(str(e))


# Modem model CRUD View
@login_required
def create_modem(request):
    """
    This View Creates the modem model object with a new payload.
    """
    form = ModemForm()
    submitted = False
    latest_records = modem.objects.all()[:10]
    if request.method == "POST":
        form = ModemForm(request.POST)
        if form.is_valid():
            form.save()
            api_key = settings.MODAM_API_KEY

            url = settings.SIX_FAB_URL
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-Key": api_key,
            }
            try:
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")
                print(f"Error Details: {error.args}")

            messages.success(request, "Modem object has been created.")
            return HttpResponseRedirect(reverse("create_modem") + "?submitted=True")
        messages.error(request, "Please Check the Form data, and try to fill again!")
        return redirect("create_modem")

    if "submitted" in request.GET:
        submitted = True

    return render(
        request,
        "modem/modem_form.html",
        {"form": form, "submitted": submitted, "latest_records": latest_records},
    )


@login_required
def update_modem(request, modem_id):
    """
    This View Update the modem model object with modem_id.
    """

    response_text = ""

    try:
        existing_modem = modem.objects.get(pk=modem_id)
    except Tag.DoesNotExist:
        messages.error(request, "Modem object isn't found.")
        return redirect("create_modem")

    form = ModemForm(instance=existing_modem)

    if request.method == "POST":
        form = ModemForm(request.POST, instance=existing_modem)

        if form.is_valid():
            form.save()

            api_key = settings.MODAM_API_KEY

            url = settings.SIX_FAB_URL
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-Key": api_key,
            }
            try:
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")
                print(f"Error Details: {error.args}")

            messages.success(request, "Modem object has been updated.")
            return redirect("create_modem")

        messages.error(request, "Please Check the Form data, and try to fill again!")
        print("Form Errors:", form.errors)
        print("POST Data:", request.POST)

    return render(
        request,
        "modem/modem_update_form.html",
        {"form": form, "response_text": response_text},
    )


@login_required
def delete_modem(request, modem_id):
    """
    This View returns the appropriate message
    like human readable after deleting the modem_id object.
    """
    if request.method == "DELETE":
        modems = get_object_or_404(modem, iccid=modem_id)
        modems.delete()
        return JsonResponse({"message": "Modem deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)


# Device model CRUD View
@login_required
def create_device(request):
    """
    This View Creates the device model object with a new payload.
    """
    form = DeviceForm()
    submitted = False
    latest_records = device.objects.all()[:10]
    if request.method == "POST":
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            api_key = settings.MODAM_API_KEY

            url = settings.SIX_FAB_URL
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-Key": api_key,
            }
            try:
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")
                print(f"Error Details: {error.args}")

            messages.success(request, "Device object has been created.")
            return HttpResponseRedirect(reverse("create_device") + "?submitted=True")

        messages.success(request, "Please Check the Form data, and try to fill again!")
        return redirect("create_device")

    if "submitted" in request.GET:
        submitted = True

    return render(
        request,
        "device/device_form.html",
        {"form": form, "submitted": submitted, "latest_records": latest_records},
    )


@login_required
def update_device(request, device_id):
    """
    This View Update the device model object with device_id.
    """

    response_text = ""

    try:
        existing_device = device.objects.get(pk=device_id)
    except Tag.DoesNotExist:
        messages.error(request, "Device object isn't found.")
        return redirect("create_tag")

    form = DeviceForm(instance=existing_device)

    if request.method == "POST":
        form = DeviceForm(request.POST, instance=existing_device)

        if form.is_valid():
            form.save()

            api_key = settings.MODAM_API_KEY

            url = settings.SIX_FAB_URL
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-Key": api_key,
            }
            try:
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")
                print(f"Error Details: {error.args}")

            messages.success(request, "Device object has been updated.")
            return redirect("create_device")

        messages.error(request, "Please Check the Form data, and try to fill again!")
        print("Form Errors:", form.errors)
        print("POST Data:", request.POST)

    return render(
        request,
        "device/device_update_form.html",
        {"form": form, "response_text": response_text},
    )


@login_required
def delete_device(request, device_id):
    """
    This View returns the appropriate message like human readable after deleting the device_id object.
    """
    if request.method == "DELETE":
        devices = get_object_or_404(device, id=device_id)
        devices.delete()
        return JsonResponse({"message": "Device deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)


# Tag model CRUD View
@login_required
def create_tag(request):
    """
    This View Creates the Tag model object with a new payload.
    """
    form = TagForm()
    submitted = False
    latest_records = Tag.objects.all()[:10]
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                api_key = settings.MODAM_API_KEY

                url = settings.SIX_FAB_URL
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "X-API-Key": api_key,
                }
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")
                print(f"Error Details: {error.args}")

            messages.success(request, "Tag data has been Created.")
            return HttpResponseRedirect(reverse("create_tag") + "?submitted=True")
        messages.error(request, "Please Check the Form data, and try to fill again!")
        return redirect("create_tag")

    if "submitted" in request.GET:
        submitted = True

    return render(
        request,
        "tag/tag_form.html",
        {"form": form, "submitted": submitted, "latest_records": latest_records},
    )


@login_required
def update_tag(request, tag_id):
    """
    This View Update the Tag model object with tag_id.
    """
    try:
        existing_tag = Tag.objects.get(pk=tag_id)
    except Exception as e:
        print(str(e))
        messages.error(request, "Tag object isn't found.")
        return redirect("create_tag")

    form = TagForm(instance=existing_tag)

    if request.method == "POST":
        form = TagForm(request.POST, instance=existing_tag)

        if form.is_valid():
            form.save()

            try:
                api_key = settings.MODAM_API_KEY

                url = settings.SIX_FAB_URL
                headers = {
                    "accept": "application/json",
                    "content-type": "application/json",
                    "X-API-Key": api_key,
                }
                response = requests.post(url, headers=headers, timeout=10)
                response.raise_for_status()
                response_text = response.text
                print(response_text)
            except requests.RequestException as error:
                print(f"Error during API request: {error}")

            messages.success(request, "Tag data has been updated.")
            return redirect("create_tag")

        messages.error(request, f"Form Errors:, {form.errors}")

    return render(
        request,
        "tag/tag_update_form.html",
        {"form": form},
    )


@login_required
def delete_tag(request, tag_id):
    """
    This View returns the appropriate message like human readable after deleting the tag_id object.
    """
    if request.method == "DELETE":
        tags = get_object_or_404(Tag, id=tag_id)
        tags.delete()
        return JsonResponse({"message": "Tag deleted successfully."}, status=200)
    return JsonResponse({"error": "Invalid request method."}, status=400)


@login_required
def device_input_view(request):
    context = {}

    try:
        form = DeviceInputForm()
        submitted = False
        latest_records = Device_inputs.objects.all()[:10]
        context["form"] = form
        context["submitted"] = submitted
        context["latest_records"] = latest_records
        if request.method == "POST":
            form = DeviceInputForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Device Input data has been Created.")
                return HttpResponseRedirect(
                    reverse("create_device_input") + "?submitted=True"
                )
            messages.error(
                request, "Please Check the Form data, and try to fill again!"
            )
            return redirect("create_device_input")

        elif "submitted" in request.GET:
            submitted = True
            context["submitted"] = submitted

    except Http404 as e:
        context["is_error"] = True
        context["error"] = str(e)
    except Exception as e:
        context["is_error"] = True
        context["error"] = str(e)
    return render(request, "device_input/device_input_form.html", context)

@login_required
def update_device_input(request, pk):
    context = {}
    try:
        existing_device_input = Device_inputs.objects.get(pk=pk)
        if not existing_device_input:
            raise Http404("Device Input Data Not Found!")
        form = DeviceInputForm(instance=existing_device_input)
        submitted = False
        context["form"] = form
        context["submitted"] = submitted
        if request.method == "POST":
            form = DeviceInputForm(request.POST, instance=existing_device_input)
            if form.is_valid():
                form.save()
                messages.success(request, "Device Input data has been Updated.")
                return HttpResponseRedirect(
                    reverse("create_device_input") + "?submitted=True"
                )
            messages.error(
                request, "Please Check the Form data, and try to fill again!"
            )
            return redirect(f"update_device_input/{pk}")

        elif "submitted" in request.GET:
            submitted = True
            context["submitted"] = submitted

    except Http404 as e:
        context["is_error"] = True
        context["error"] = str(e)
        return redirect("create_device_input")
    except Exception as e:
        context["is_error"] = True
        context["error"] = str(e)
    return render(request, "device_input/device_input_update_form.html", context)

@login_required
def delete_device_input(request, pk):
    if request.method == "DELETE":
        device_inputes = get_object_or_404(Device_inputs, id=pk)
        device_inputes.delete()
        return JsonResponse(
            {"message": "Device Inputs deleted successfully."}, status=200
        )
    return JsonResponse({"error": "Invalid request method."}, status=400)

from bokeh.plotting import curdoc, figure, show
from bokeh.layouts import column, layout,row
from django.db import connections
import cartopy.crs as ccrs

def fetch_energy_data(val):
    if len(val) == 0 : return []
    placeholders = ', '.join(['%s'] * len(val))
    sql_query = f"SELECT * FROM mft_rrc_texas_gov_shp_table WHERE oper_nm IN ({placeholders})"

    try:
        with connections['third_db'].cursor() as cursor:
            cursor.execute(sql_query, val)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            data = [dict(zip(columns, row)) for row in rows]
            return data

    except Exception as e:
        print(f'An error occurred while fetching energy data: {e}')
        return []

def fetch_oper_nm():
    try:
        sql_query = "SELECT DISTINCT oper_nm FROM mft_rrc_texas_gov_shp_table;"

        with connections['third_db'].cursor() as cursor:
            cursor.execute(sql_query)
            rows = cursor.fetchall()
            data = [row[0] for row in rows]
            return data

    except Exception as e:
        print(f'An error occurred while fetching oper_nm: {e}')
        return []

def energy(request):
    params_lst = request.GET.getlist('filter_by[]', [])
    gv.extension('bokeh', 'matplotlib')
    # folder_path = settings.BASE_DIR + f'/downloads/documents_20240327'
    # items = sorted(os.listdir(folder_path))

    # shp_obj = ReadSHP(folder_path)
    # shp_data = shp_obj.read_shp()
    
    shp_data = fetch_energy_data(params_lst)
    print(f"==>> shp_data: {shp_data}")
    items = fetch_oper_nm()
    
    # df = pd.DataFrame(shp_data)
    # gdf = gpd.GeoDataFrame(df, geometry='geometry', crs='EPSG:4326')
    # gdf_element = gv.Path(gdf, vdims=['P5_NUM', 'T4PERMIT', 'DIAMETER'])
    # features = gv.Overlay([gf.land, gf.borders, gf.coastline])
    # hover = HoverTool(tooltips=[("DIAMETER", "@DIAMETER")])
    # features = features*gdf_element.opts(tools=[hover])
    # features.opts(projection=crs.LambertCylindrical(), global_extent=True, width=500, height=250)
    # plot = gv.render(features, backend='bokeh', size=200)
    
    rows = []
    if len(shp_data) > 0 and len(items) > 0:
        for data in shp_data:
            tpms_id = data['tpms_id']
            diameter = float(data['diameter'])
            geometry = data['geometry']
            if geometry['type'] == 'MultiLineString':
                coordinates = geometry['coordinates']
                line_strings = [LineString(coords) for coords in coordinates]
                geometry = MultiLineString(line_strings)
            elif geometry['type'] == 'LineString':
                coordinates = geometry['coordinates']
                geometry = LineString(coordinates)
            
            rows.append({'tpms_id': tpms_id, 'diameter': diameter, 'geometry': geometry})

        gdf = gpd.GeoDataFrame(rows, geometry='geometry')

        gdf_element = gv.Path(gdf, vdims=['tpms_id', 'diameter'])
        features = gv.Overlay([gf.land, gf.borders, gf.coastline])
        hover = HoverTool(tooltips=[("DIAMETER", "@diameter")])
        features = features*gdf_element.opts(tools=[hover])
        features.opts(projection=ccrs.LambertCylindrical(), global_extent=True, width=500, height=250)
    else:
        features = gv.Overlay([gf.land, gf.borders, gf.coastline])
        features.opts(projection=ccrs.LambertCylindrical(), global_extent=True, width=500, height=250)

    plot = gv.render(features, backend='bokeh', size=200)

    script, div = components(plot)
    
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 6, 4, 5]
    
    curdoc().theme = 'caliber'

    p = figure(title='caliber', width=300, height=300)
    p.line(x, y)
    dropdown_options = ["1 day", "1 week", "1 month"]
    select = Select( value="1 day", options=dropdown_options)
    plot = column([select, p], sizing_mode='stretch_both')
    
    script1, div1 = components(plot)

    context = {
        'script': script, 
        'div': div,
        'files':items,
        'shp_data':shp_data,
        'script1':script1,
        'div1':div1,
        }
    return render(request, 'Energy.html', context)




