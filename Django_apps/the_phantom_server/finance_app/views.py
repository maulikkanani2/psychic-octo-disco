"""
_summary_

Returns:
    _type_: This View file returns all finance-related data.
"""

from datetime import datetime
from io import BytesIO
import csv
import json
import requests
import pandas as pd
import re

from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import get_template
from django.db.models import Sum, Prefetch, F
from django.db.models.functions import TruncMonth
from django.contrib.auth.decorators import login_required
from django.conf import settings

from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet

from xhtml2pdf import pisa

from bokeh.plotting import figure
from bokeh.embed import components

from dateutil.relativedelta import relativedelta
from the_phantom_server.utils import (
    financial_Data_Processor,
    double_line_regular_chart,
    df_calcs,
    LOS_columns,
    oil_data,
    gas_data,
    ngl_data,
    total_rev_data,
    gathering_and_Processing_data,
    single_line_date_chart_day,
)
from API.views import transdata
from .models import Trans

import logging

logger = logging.getLogger(__name__)

########################
# data_cleaner placeholder
pd.set_option("display.max_columns", None)


def unitcost(dataframe, revenue, units):
    # Make a copy of original dataframe.
    # It's a good practice so that the original dataframe isn't modified when we don't want it to.
    df = dataframe.copy()
    df["unitcost"] = df[revenue].div(df[units])
    return df


#########################
####


def create_alias_mapping(df, column1, column2):
    # Creating a dictionary for alias mapping
    alias_mapping = dict(zip(df[column1], df[column2]))

    return alias_mapping


def merge_dataframes(df1, df2, common_column, how="inner"):
    """
    Merge two data frames on a common column.

    :param df1: First DataFrame.
    :param df2: Second DataFrame.
    :param common_column: The name of the column to merge on.
    :param how: Type of merge to be performed.
               'left': use only keys from left frame (SQL left outer join)
               'right': use only keys from right frame (SQL right outer join)
               'outer': use union of keys from both frames (SQL full outer join)
               'inner': use intersection of keys from both frames (SQL inner join)
    :return: Merged DataFrame.
    """
    return pd.merge(df1, df2, on=common_column, how=how)


def process_data(queryset):
    # Convert queryset to DataFrame
    df = pd.DataFrame(list(queryset))
    # Further data processing here
    return df


def rename_columns(df, value_columns=None, new_column_names=None):
    if value_columns is None or new_column_names is None:
        # Handle the case where one or both parameters are not provided
        raise ValueError("Both value_columns and new_column_names must be provided")

    if len(value_columns) != len(new_column_names):
        # Handle the case where the length of the lists don't match
        raise ValueError(
            "value_columns and new_column_names must be of the same length"
        )

    rename_dict = {old: new for old, new in zip(value_columns, new_column_names)}
    df.rename(columns=rename_dict, inplace=True)
    return df


@login_required
def loe_analytics(request):
    # Data for the charts (replace with your actual data)
    data_line_chart1 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    # Create Bokeh charts
    line_chart1 = double_line_regular_chart(data_line_chart1)

    # Embed the charts in the HTML template
    script_line_chart1, div_line_chart1 = components(line_chart1)
    popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)

    context = {
        "script_line_chart1": script_line_chart1,
        "div_line_chart1": div_line_chart1,
        "popup_script_line_chart1": popup_script_line_chart1,
        "popup_div_line_chart1": popup_div_line_chart1,
    }
    return render(request, "loe_analytics.html", context)


@login_required
def spend_analysis(request):
    # Data for the charts (replace with your actual data)
    data_line_chart1 = {
        "x_values": [1, 2, 3, 4, 5],
        "y_values": [10, 8, 6, 4, 2],
        "y2_values": [8, 12, 16, 24, 32],
    }

    # Create Bokeh charts
    line_chart1 = double_line_regular_chart(data_line_chart1)

    # Embed the charts in the HTML template
    script_line_chart1, div_line_chart1 = components(line_chart1)
    popup_script_line_chart1, popup_div_line_chart1 = components(line_chart1)

    context = {
        "script_line_chart1": script_line_chart1,
        "div_line_chart1": div_line_chart1,
        "popup_script_line_chart1": popup_script_line_chart1,
        "popup_div_line_chart1": popup_div_line_chart1,
    }
    return render(request, "spend_analysis.html", context)


# Your Django view function


def financial(request):
    """
    This function returns the Trans API response and Chart data.
    """

    months_ago = datetime.now() - relativedelta(
        months=5
    )  # drop filter into this from HTML
    print(months_ago)
    # Define prefetch_related options
    prefetch = Prefetch("acct")
    # Define your queryset with filtering conditions
    period = "acctg_period"
    gross_gen_acc = [
        410,
        415,
        420,
        430,
        440,
        450,
        470,
        481,
        490,
        510,
        515,
        800,
        811,
        820,
        830,
        840,
        850,
        860,
        870,
        875,
        880,
        881,
        883,
        888,
        882,
        884,
        885,
    ]
    gross_columns = [
        "acct__name",
        period,
        "stat1_amt",
        "stat1_qty1",
        "gen_acc",
        "gen_acc__name",
    ]
    net_gen_acc = [
        150,
        159,
        151,
        152,
        153,
        154,
        156,
        155,
        157,
        158,
        410,
        415,
        420,
        430,
        440,
        450,
        470,
        481,
        490,
        510,
        515,
        520,
        525,
        530,
        540,
    ]
    net_columns = ["acct__name", period, "AMT", "QTY1", "gen_acc"]
    request_type = "gross"
    # as per your gross / net_accounts logic
    if request_type == "gross":
        gen_acc_code = gross_gen_acc
        cols = gross_columns
        amount = "stat1_amt"
        qty = "stat1_qty1"
    else:
        gen_acc_code = net_gen_acc
        cols = net_columns
        amount = "AMT"
        amount = "QTY1"

    queryset = (
        Trans.objects.only(*cols)
        .filter(**{"%s__gte" % period: months_ago, "gen_acc__in": gen_acc_code})
        .prefetch_related(prefetch)
        .annotate(month=TruncMonth(period))  # Replace 'date' with actual date field
        .annotate(
            Period=F(period),
            Amount=F(amount),
            Qty=F(qty),
            Account_name=F("acct__name"),
            Gen_account=F("gen_acc__name"),
        )
        .values("Period", "Amount", "Qty", "Account_name", "Gen_account")
        .annotate(total_amount=Sum("Amount"))  # Use new field name
        .order_by("Period")  # Use new field name
    )
    # after the database model query has aggregated the data the remainder is done in pandas
    df = pd.DataFrame(queryset, index=None)
    # apply standard calcs
    df = df_calcs(df, "Amount", "Qty")
    df.to_csv("/Users/jongrottis/Documents/my_csv_file.csv", index=False)
    print(df)
    date_column_names = LOS_columns(df)
    print(date_column_names)
    # Datasets for rendering in HTML
    oil_data_amount_pivot, oil_data_qty_pivot, oil_data_bbl_pivot = oil_data(df)
    gas_data_amount_pivot, gas_data_qty_pivot, gas_data_mcf_pivot = gas_data(df)
    ngl_data_amount_pivot, ngl_data_qty_pivot, ngl_data_bbl_pivot = ngl_data(df)
    total_revenue_amount_pivot, total_revenue_qty_pivot, total_revenue_bbl_pivot = (
        total_rev_data(df)
    )
    total_G_and_P_amount_pivot = gathering_and_Processing_data(df)

    # Bokeh Plotting

    # print(df_pivot)

    x_values = list(df.columns)
    y_values = list(df.index)
    data_values = [list(df[col]) for col in x_values]

    plot = figure(
        x_range=x_values,
        height=350,
        title="Bokeh Chart Example",
        toolbar_location=None,
        tools="",
        y_axis_label="Amount",
    )

    for i, y_value in enumerate(y_values):
        if i < len(data_values):  # Check if i is within the range of data_values
            plot.line(x=x_values, y=data_values[i], line_width=2)

    plot.legend.location = "top_left"
    plot.legend.click_policy = "hide"

    script, div = components(plot)
    return render(
        request,
        "Financials.html",
        {
            "queryset": queryset,
            "oil_amount": oil_data_amount_pivot,
            "oil_data_qty_pivot": oil_data_qty_pivot,
            "oil_data_bbl_pivot": oil_data_bbl_pivot,
            "gas_data_amount_pivot": gas_data_amount_pivot,
            "gas_data_qty_pivot": gas_data_qty_pivot,
            "gas_data_mcf_pivot": gas_data_mcf_pivot,
            "ngl_data_amount_pivot": ngl_data_amount_pivot,
            "ngl_data_qty_pivot": ngl_data_qty_pivot,
            "ngl_data_bbl_pivot": ngl_data_bbl_pivot,
            "total_revenue_amount_pivot": total_revenue_amount_pivot,
            "total_G_and_P_amount_pivot": total_G_and_P_amount_pivot,
            "column_names": date_column_names,
            "bokeh_script": script,
            "bokeh_div": div,
        },
    )


@login_required
def financialview(request):
    # Make a GET request to your REST API
    # response = requests.get(settings.TRANS_API_URL)
    context = {}
    roles = request.user.session_token.get('roles') if request.user.session_token.get('roles') else []
    if f'{settings.DESCOPE_IS_FINANCE_ROLE}' not in roles:
        context[f"{settings.DESCOPE_IS_FINANCE_ROLE}"] = False
    else:
        response = transdata(request)

        # If the request was successful, parse the data
        if response.status_code == 200:
            queryset = response.data
            # Initialize the financial_Data_Processor class
            df = financial_Data_Processor(queryset).to_dataframe()
            # Fetch unique date columns
            date_column_names = financial_Data_Processor(queryset).date_columns()
            # print(date_column_names)
            # calculated and aggregated data
            # financial_data = fdp.aggregate_account()
            print("dataframe")
            # print(fdp.to_dataframe())
            print("end")

            # create oil data - filter condensate and oil -aggregate - run base calcs and drop unnecessary
            oil_data = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account", ["CONDENSATE SALES", "OIL SALES", "OIL MARKETING SALES"]
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            oil_data_net_revenue = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account", ["CONDENSATE SALES", "OIL SALES", "OIL MARKETING SALES"]
                )
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .to_list_of_dicts()
            )

            gas_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["GAS SALES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            gas_data_net_revenue = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["GAS SALES"])
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .to_list_of_dicts()
            )

            ngl_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["LIQUID SALES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            ngl_data_net_revenue = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["LIQUID SALES"])
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .to_list_of_dicts()
            )

            total_revenue_data = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LIQUID SALES", "GAS SALES", "CONDENSATE SALES", "OIL SALES"],
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            g_and_p_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["COST OF OIL & GAS REVENUE"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            production_taxes_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["PRODUCTION TAXES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )

            net_revenue_after_deductions = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    [
                        "LIQUID SALES",
                        "GAS SALES",
                        "CONDENSATE SALES",
                        "OIL SALES",
                        "PRODUCTION TAXES",
                        "COST OF OIL & GAS REVENUE",
                    ],
                )
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .  # to_dataframe())
                # net_revenue_after_deductions.to_csv('/Users/jongrottis/Documents/net_rev.csv', index=False)
                to_list_of_dicts()
            )
            # print(net_revenue_after_deductions)
            lease_operating_expenses_data = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .aggregate_account(["Period"]).base_calcs().drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()  # drop_columns(['Gen_account', 'gen_acc','LOS_aggregation']). \
            )
            
            lease_operating_expenses = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .aggregate_account(["Account_name", "Period", "Gen_account"])
                .to_dataframe()  # drop_columns(['Gen_account', 'gen_acc','LOS_aggregation']). \
            ).reset_index()

            lease_operating_expenses_net_revenue = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .to_list_of_dicts()
            )

            lease_operating_expenses = {
                name: {
                    "Period": group["Period"].values.tolist(),
                    "Amount": [round(data, 2) for data in group["Amount"].values.tolist()],
                }
                for name, group in lease_operating_expenses.groupby("Account_name")
            }

            total_LOE = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(["Gen_account", "gen_acc", "total_amount", "Account_name"])
                .to_list_of_dicts()
            )
            # lease_operating_expenses=lease_operating_expenses.to_dict('records')
            # print(lease_operating_expenses)
            # output_dict = df_grouped.to_dict('list') # or 'series'
            # output_dict = df_grouped.to_dict('index')
            # output_dict = df_grouped.to_dict('records')
            # Data for the charts (replace with your actual data)
            data_line_chart1 = {
                "x_values": [1, 2, 3, 4, 5],
                "y_values": [10, 8, 6, 4, 2],
                "y2_values": [8, 12, 16, 24, 32],
            }
            # Create Bokeh charts
            line_chart1 = double_line_regular_chart(data_line_chart1)
            # Embed the charts in the HTML template
            script_line_chart1, div_line_chart1 = components(line_chart1)
            popup_script_line_chart1, popup_sdiv_line_chart1 = components(line_chart1)

            if len(gas_data) > 1:
                gas_data_chart = single_line_date_chart_day(
                    data=gas_data,
                    x_column="Period",
                    y_column="Amount",
                    y_axis_label="BBls",
                    x_axis_label="Period",
                    legend_label = 'Volume',
                )
                script_gas_data_chart, div_gas_data_chart = components(gas_data_chart)
                popup_script_gas_data_chart, popup_div_gas_data_chart = components(gas_data_chart)
            else:
                script_gas_data_chart = None
                div_gas_data_chart = None
                popup_script_gas_data_chart = None
                popup_div_gas_data_chart = None

            if len(oil_data) > 1:
                oil_data_chart = single_line_date_chart_day(
                    data=oil_data,
                    x_column="Period",
                    y_column="Amount",
                    y_axis_label="BBls",
                    x_axis_label="Period",
                    legend_label = 'Volume',
                )
                script_oil_data_chart, div_oil_data_chart = components(oil_data_chart)
                popup_script_oil_data_chart, popup_div_oil_data_chart = components(oil_data_chart)
            else:
                script_oil_data_chart = None
                div_oil_data_chart = None
                popup_script_oil_data_chart = None
                popup_div_oil_data_chart = None
                
            if len(ngl_data) > 1:
                ngl_data_chart = single_line_date_chart_day(
                    data=ngl_data,
                    x_column="Period",
                    y_column="Amount",
                    y_axis_label="BBls",
                    x_axis_label="Period",
                    legend_label = 'Volume',
                )
                script_ngl_data_chart, div_ngl_data_chart = components(ngl_data_chart)
                script_ngl_data_chart, div_ngl_data_chart = components(ngl_data_chart)
                popup_script_ngl_data_chart, popup_div_ngl_data_chart = components(ngl_data_chart)
            else:
                script_ngl_data_chart = None
                div_ngl_data_chart = None
                popup_script_ngl_data_chart = None
                popup_div_ngl_data_chart = None
            
            if len(lease_operating_expenses_data) > 1:
                lease_operating_expenses_data_chart = single_line_date_chart_day(
                    data=lease_operating_expenses_data,
                    x_column="Period",
                    y_column="Amount",
                    y_axis_label="BBls",
                    x_axis_label="Period",
                    legend_label = 'Volume',
                )
                script_lease_operating_expenses_data_chart, div_lease_operating_expenses_data_chart = components(lease_operating_expenses_data_chart)
                popup_script_lease_operating_expenses_data_chart, popup_div_lease_operating_expenses_data_chart = components(lease_operating_expenses_data_chart)
            else:
                script_lease_operating_expenses_data_chart = None
                div_lease_operating_expenses_data_chart = None
                popup_script_lease_operating_expenses_data_chart = None
                popup_div_lease_operating_expenses_data_chart = None
            
            return render(
                request,
                "Financials.html",
                {
                    "ngl_data": ngl_data,
                    "gas_data": gas_data,
                    "oil_data": oil_data,
                    "column_names": date_column_names,
                    "total_revenue_data": total_revenue_data,
                    "g_and_p_data": g_and_p_data,
                    "production_taxes_data": production_taxes_data,
                    "net_revenue_after_deductions": net_revenue_after_deductions,
                    "lease_operating_expenses": lease_operating_expenses,
                    "total_LOE": total_LOE,
                    "script_line_chart1": script_line_chart1,
                    "div_line_chart1": div_line_chart1,
                    "popup_script_line_chart1": popup_script_line_chart1,
                    "popup_div_line_chart1": popup_sdiv_line_chart1,
                    "range": request.GET.get("range"),
                    "period": request.GET.get("period"),
                    "col_length": len(date_column_names) + 1,
                    "gas_data_net_revenue": gas_data_net_revenue,
                    "oil_data_net_revenue": oil_data_net_revenue,
                    "ngl_data_net_revenue": ngl_data_net_revenue,
                    "lease_operating_expenses_net_revenue": lease_operating_expenses_net_revenue,
                    "is_finance":True,
                    
                    "script_gas_data_chart":script_gas_data_chart,
                    "div_gas_data_chart":div_gas_data_chart,
                    "script_ngl_data_chart":script_ngl_data_chart,
                    "div_ngl_data_chart":div_ngl_data_chart,
                    "script_oil_data_chart":script_oil_data_chart,
                    "div_oil_data_chart":div_oil_data_chart,
                    "script_lease_operating_expenses_data_chart":script_lease_operating_expenses_data_chart,
                    "div_lease_operating_expenses_data_chart":div_lease_operating_expenses_data_chart,
                    
                    "popup_script_gas_data_chart":popup_script_gas_data_chart,
                    "popup_div_gas_data_chart":popup_div_gas_data_chart,
                    "popup_script_ngl_data_chart":popup_script_ngl_data_chart,
                    "popup_div_ngl_data_chart":popup_div_ngl_data_chart,
                    "popup_script_oil_data_chart":popup_script_oil_data_chart,
                    "popup_div_oil_data_chart":popup_div_oil_data_chart,
                    "popup_script_lease_operating_expenses_data_chart":popup_script_lease_operating_expenses_data_chart,
                    "popup_div_lease_operating_expenses_data_chart":popup_div_lease_operating_expenses_data_chart,
                },
            )
    return render(request,"Financials.html",context)
        


def gas_sales_pdf(request):
    try:
        response = transdata(request)

        # If the request was successful, parse the data
        if response.status_code == 200:
            queryset = response.data
            # Initialize the financial_Data_Processor class
            df = financial_Data_Processor(queryset).to_dataframe()
            # Fetch unique date columns
            date_column_names = financial_Data_Processor(queryset).date_columns()
            # print(date_column_names)
            # calculated and aggregated data
            # financial_data = fdp.aggregate_account()
            print("dataframe")
            # print(fdp.to_dataframe())
            print("end")

            # create oil data - filter condensate and oil -aggregate - run base calcs and drop unnecessary
            oil_data = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["CONDENSATE SALES", "OIL SALES", "OIL MARKETING SALES"],
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            gas_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["GAS SALES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            ngl_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["LIQUID SALES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            total_revenue_data = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LIQUID SALES", "GAS SALES", "CONDENSATE SALES", "OIL SALES"],
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            g_and_p_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["COST OF OIL & GAS REVENUE"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            production_taxes_data = (
                financial_Data_Processor(queryset)
                .filter_column("Gen_account", ["PRODUCTION TAXES"])
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            net_revenue_after_deductions = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    [
                        "LIQUID SALES",
                        "GAS SALES",
                        "CONDENSATE SALES",
                        "OIL SALES",
                        "PRODUCTION TAXES",
                        "COST OF OIL & GAS REVENUE",
                    ],
                )
                .net_revenue()
                .aggregate_account("Period")
                .drop_columns(
                    [
                        "Gen_account",
                        "gen_acc",
                        "total_amount",
                        "Account_name",
                        "Amount",
                        "Qty",
                        "LOS_aggregation",
                    ]
                )
                .  # to_dataframe())
                # net_revenue_after_deductions.to_csv('/Users/jongrottis/Documents/net_rev.csv', index=False)
                to_list_of_dicts()
            )
            # print(net_revenue_after_deductions)
            lease_operating_expenses = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .aggregate_account(["Account_name", "Period", "Gen_account"])
                .to_dataframe()  # drop_columns(['Gen_account', 'gen_acc','LOS_aggregation']). \
            ).reset_index()
            # lease_operating_expenses.reset_index().to_csv('/Users/jongrottis/Documents/loe2.csv', index=False)
            # to_list_of_dicts())
            lease_operating_expenses1 = {}
            for name, group in lease_operating_expenses.groupby("Account_name"):
                new = []
                for i in group["Period"]:
                    data = {
                        "Period": i,
                        "Amount": group.loc[group["Period"] == i, "Amount"].iloc[0],
                    }
                    new.append(data)
                lease_operating_expenses1[name] = new

            lease_operating_expenses = lease_operating_expenses1

            # lease_operating_expenses = {
            #     name: {
            #         'Period': group['Period'].values.tolist(),
            #         'Amount': [round(data, 2) for data in group['Amount'].values.tolist()]
            #     }
            #     for name, group in lease_operating_expenses.groupby('Account_name')
            # }

            total_LOE = (
                financial_Data_Processor(queryset)
                .filter_column(
                    "Gen_account",
                    ["LEASE OPERATING EXPENSE (LOE)", "LEASE OPERATING EXPENSES (LOE)"],
                )
                .aggregate_account("Period")
                .base_calcs()
                .drop_columns(
                    ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                )
                .to_list_of_dicts()
            )

            context = {
                "ngl_data": ngl_data,
                "gas_data": gas_data,
                "oil_data": oil_data,
                "column_names": date_column_names,
                "total_revenue_data": total_revenue_data,
                "g_and_p_data": g_and_p_data,
                "production_taxes_data": production_taxes_data,
                "net_revenue_after_deductions": net_revenue_after_deductions,
                "lease_operating_expenses": lease_operating_expenses,
                "total_LOE": total_LOE,
            }

            return render(request, "exports/accounts_pdf.html", context)
            # template = get_template("exports/gas_sales_pdf.html")
            # html = template.render(context)
            # result = BytesIO()
            # pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
            # if not pdf.err:
            #     response = HttpResponse(result.getvalue(), content_type='applocation/pdf')
            #     response['Content-Disposition'] = 'attachment; filename="gas_sales.pdf"'
            #     return response
    except Exception as e:
        return HttpResponse(str(e))


class exports_data(ViewSet):
    """
    This class exports the PDF and CSV files.
    """

    @action(methods=["get"], detail=False, url_path="accounts_pdf")
    def download_accounts_pdf(self, request):
        """
        This function creates the PDF file and returns it.
        """
        try:
            filter_range = request.GET.get("range")
            filter_period = request.GET.get("period")
            params = {"range": filter_range, "period": filter_period}
            response = (
                requests.get(settings.TRANS_API_URL, params=params, timeout=20)
                if filter_range or filter_period
                else requests.get(settings.TRANS_API_URL, timeout=20)
            )
            if response.status_code == 200:
                queryset = response.json()
                date_column_names = financial_Data_Processor(queryset).date_columns()
                oil_data = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        ["CONDENSATE SALES", "OIL SALES", "OIL MARKETING SALES"],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                gas_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["GAS SALES"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                ngl_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["LIQUID SALES"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                total_revenue_data = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        ["LIQUID SALES", "GAS SALES", "CONDENSATE SALES", "OIL SALES"],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                g_and_p_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["COST OF OIL & GAS REVENUE"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                production_taxes_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["PRODUCTION TAXES"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )
                net_revenue_after_deductions = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        [
                            "LIQUID SALES",
                            "GAS SALES",
                            "CONDENSATE SALES",
                            "OIL SALES",
                            "PRODUCTION TAXES",
                            "COST OF OIL & GAS REVENUE",
                        ],
                    )
                    .net_revenue()
                    .aggregate_account("Period")
                    .drop_columns(
                        [
                            "Gen_account",
                            "gen_acc",
                            "total_amount",
                            "Account_name",
                            "Amount",
                            "Qty",
                            "LOS_aggregation",
                        ]
                    )
                    .to_list_of_dicts()
                )
                lease_operating_expenses = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        [
                            "LEASE OPERATING EXPENSE (LOE)",
                            "LEASE OPERATING EXPENSES (LOE)",
                        ],
                    )
                    .aggregate_account(["Account_name", "Period", "Gen_account"])
                    .to_dataframe()
                ).reset_index()
                lease_operating_expenses1 = {}
                for name, group in lease_operating_expenses.groupby("Account_name"):
                    new = []
                    for i in group["Period"]:
                        data = {
                            "Period": i,
                            "Amount": group.loc[group["Period"] == i, "Amount"].iloc[0],
                        }
                        new.append(data)
                    lease_operating_expenses1[name] = new

                lease_operating_expenses = lease_operating_expenses1
                # lease_operating_expenses = {
                #     name: {
                #         'Period': group['Period'].values.tolist(),
                #         'Amount': [round(data, 2) for data in group['Amount'].values.tolist()]
                #     }
                #     for name, group in lease_operating_expenses.groupby('Account_name')
                # }

                total_LOE = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        [
                            "LEASE OPERATING EXPENSE (LOE)",
                            "LEASE OPERATING EXPENSES (LOE)",
                        ],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )
                context = {
                    "ngl_data": ngl_data,
                    "gas_data": gas_data,
                    "oil_data": oil_data,
                    "column_names": date_column_names,
                    "total_revenue_data": total_revenue_data,
                    "g_and_p_data": g_and_p_data,
                    "production_taxes_data": production_taxes_data,
                    "net_revenue_after_deductions": net_revenue_after_deductions,
                    "lease_operating_expenses": lease_operating_expenses,
                    "total_LOE": total_LOE,
                }
                template = get_template("exports/accounts_pdf.html")
                html = template.render(context)
                result = BytesIO()
                pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
                if not pdf.err:
                    response = HttpResponse(
                        result.getvalue(), content_type="applocation/pdf"
                    )
                    response["Content-Disposition"] = (
                        'attachment; filename="accounts_pdf.pdf"'
                    )
                    return response
        except Exception as e:
            return HttpResponse(str(e))

    @action(methods=["get"], detail=False, url_path="accounts_csv")
    def download_accounts_csv(self, request):
        """
        This function creates the CSV file and returns it.
        """
        try:
            filter_range = request.GET.get("range")
            filter_period = request.GET.get("period")
            params = {"range": filter_range, "period": filter_period}
            response = (
                requests.get(settings.TRANS_API_URL, params=params, timeout=20)
                if filter_range or filter_period
                else requests.get(settings.TRANS_API_URL, timeout=20)
            )
            if response.status_code == 200:
                queryset = response.json()
                date_column_names = financial_Data_Processor(queryset).date_columns()
                oil_data = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        ["CONDENSATE SALES", "OIL SALES", "OIL MARKETING SALES"],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                gas_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["GAS SALES"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                ngl_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["LIQUID SALES"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                total_revenue_data = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        ["LIQUID SALES", "GAS SALES", "CONDENSATE SALES", "OIL SALES"],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                g_and_p_data = (
                    financial_Data_Processor(queryset)
                    .filter_column("Gen_account", ["COST OF OIL & GAS REVENUE"])
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                lease_operating_expenses = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        [
                            "LEASE OPERATING EXPENSE (LOE)",
                            "LEASE OPERATING EXPENSES (LOE)",
                        ],
                    )
                    .aggregate_account(["Account_name", "Period", "Gen_account"])
                    .to_dataframe()
                ).reset_index()

                lease_operating_expenses = {
                    name: {
                        "Period": group["Period"].values.tolist(),
                        "Amount": [
                            round(data, 2) for data in group["Amount"].values.tolist()
                        ],
                    }
                    for name, group in lease_operating_expenses.groupby("Account_name")
                }

                total_LOE = (
                    financial_Data_Processor(queryset)
                    .filter_column(
                        "Gen_account",
                        [
                            "LEASE OPERATING EXPENSE (LOE)",
                            "LEASE OPERATING EXPENSES (LOE)",
                        ],
                    )
                    .aggregate_account("Period")
                    .base_calcs()
                    .drop_columns(
                        ["Gen_account", "gen_acc", "total_amount", "Account_name"]
                    )
                    .to_list_of_dicts()
                )

                rows = ["Account"]
                rows.extend(date_column_names)

                response = HttpResponse(content_type="text/csv")
                response["Content-Disposition"] = (
                    'attachment; filename="accounts_csv.csv"'
                )
                writer = csv.writer(response)
                writer.writerow(rows)
                if len(gas_data) > 0:
                    writer.writerow(["<<======Gas Data=======>>"])
                    Volume = ["Volume (MCF)"]
                    Revenue = ["Revenue"]
                    Ave_Price = ["Ave Price Per MCF"]
                    for data in gas_data:
                        Volume.append(data["Qty"])
                        Revenue.append(data["Amount"])
                        Ave_Price.append(data["unitcost"])

                    [writer.writerow(Volume)]
                    [writer.writerow(Revenue)]
                    [writer.writerow(Ave_Price)]

                if len(oil_data) > 0:
                    writer.writerow(["<<======OIL AND CONDENSATE SALES=======>>"])
                    Volume = ["Volume (BBLS)"]
                    Revenue = ["Revenue"]
                    Ave_Price = ["Ave Price Per BBl"]
                    for data in oil_data:
                        Volume.append(data["Qty"])
                        Revenue.append(data["Amount"])
                        Ave_Price.append(data["unitcost"])
                    [writer.writerow(Volume)]
                    [writer.writerow(Revenue)]
                    [writer.writerow(Ave_Price)]

                if len(ngl_data) > 0 and len(g_and_p_data) > 0:
                    writer.writerow(["<<======NATURAL GAS LIQUIDS SALES=======>>"])
                    Volume = ["Volume (BBLs)"]
                    Revenue = ["Revenue"]
                    Ave_Price = ["Ave Price Per BBls"]
                    g_and_p = ["Gathering and Marketing Fees"]
                    for data in ngl_data:
                        Volume.append(data["Qty"])
                        Revenue.append(data["Amount"])
                        Ave_Price.append(data["unitcost"])
                    for data in g_and_p_data:
                        g_and_p.append(data["Amount"])
                    [writer.writerow(Volume)]
                    [writer.writerow(Revenue)]
                    [writer.writerow(Ave_Price)]
                    [writer.writerow(g_and_p)]

                if len(total_revenue_data) > 0:
                    revenue = ["TOTAL SALES REVENUE"]
                    for data in total_revenue_data:
                        revenue.append(round(data["Amount"], 2))
                    writer.writerow(revenue)

                if isinstance(lease_operating_expenses, dict):
                    writer.writerow(["<<======LEASE OPERATING EXPENSES=======>>"])
                    row_data = []
                    for account, data in lease_operating_expenses.items():
                        lease_data = [account]
                        [lease_data.append(i) for i in data["Amount"]]
                        row_data.append(lease_data)
                    [writer.writerow(data) for data in row_data]

                if len(total_LOE) > 0:
                    lease = ["TOTAL LEASE OPERATING EXPENSES"]
                    for data in total_LOE:
                        lease.append(round(data["Amount"], 2))
                    writer.writerow(lease)

                writer.writerow(["<<======EXPENSES=======>>"])
                row_data = [
                    ["", "Subcategory B.1", "Description B.1"],
                    ["", "Subcategory B.2", "Description B.2"],
                    ["", "Subcategory B.3", "Description B.3"],
                ]
                [writer.writerow(data) for data in row_data]
                return response
        except Exception as e:
            return HttpResponse(str(e))
