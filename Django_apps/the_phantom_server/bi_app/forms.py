from django import forms
from django.forms import ModelForm, modelformset_factory, BaseModelFormSet
from django.utils import timezone
from bi_app.models import (
    Docgasmeterreadings,
    Doccompressors,
    Docruntickets,
    Docwellheadpressures,
    Docwaterdisposition,
    Docwelltests,
    modem,
    Tag,
    device,
    Device_inputs,
)
from API.views import device_list, tag_list, modem_list
import datetime

# create a gasmeter form


class GasMeterForm(ModelForm):
    class Meta:
        # bring in model but I can also adjust and filter the model here
        model = Docgasmeterreadings
        fields = [
            "docdate",
            "docidgasmeterreadings",
            "userid",
            "temperature",
            "volume",
            "linepressure",
            "inputbyid",
        ]
        widgets = {
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "docidgasmeterreadings": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Gas meter Readings",
                }
            ),
            "userid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The User ID",
                }
            ),
            "temperature": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Temperature",
                }
            ),
            "volume": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Volume",
                }
            ),
            "linepressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Line pressure",
                }
            ),
            "inputbyid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Input by ID",
                }
            ),
        }
        # Add other widgets here as needed

    def __init__(self, *args, **kwargs):
        super(GasMeterForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class DocCompressorsForm(ModelForm):
    class Meta:
        # bring in model but I can also adjust and filter the model here
        model = Doccompressors
        fields = [
            "ambienttemp",
            "dischargetemperature",
            "suctiontemperature",
            "watertemp",
            "oilpressure",
            "oiltemp",
            "rpm",
            "suctionpressure",
            "userid",
            "docdate",
        ]
        widgets = {
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "ambienttemp": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Ambient Temperature",
                }
            ),
            "dischargetemperature": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Discharge Temperature",
                }
            ),
            "suctiontemperature": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Suction Temperature",
                }
            ),
            "watertemp": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Water Temperature",
                }
            ),
            "oilpressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Oil Pressure",
                }
            ),
            "oiltemp": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Oil Temperature",
                }
            ),
            "rpm": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The RPM"}
            ),
            "suctionpressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Suction Pressure",
                }
            ),
            "userid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The User ID",
                }
            ),
        }
        # Add other widgets here as needed

    def __init__(self, *args, **kwargs):
        super(DocCompressorsForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class DocrunticketsForm(ModelForm):
    class Meta:
        model = Docruntickets
        fields = [
            "end_ft",
            "end_inch",
            "end_qtr",
            "gravity",
            "bsw",
            "docdate",
            "purchaserid",
            "ticketnum",
            "volume",
        ]

        # Add other widgets here as needed
        widgets = {
            "end_ft": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The End Feet",
                }
            ),
            "end_inch": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The End Inch",
                }
            ),
            "end_qtr": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The End 1/4",
                }
            ),
            "gravity": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Gravity",
                }
            ),
            "bsw": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The BSW"}
            ),
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "purchaserid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Purchaser ID",
                }
            ),
            "ticketnum": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Ticket Number",
                }
            ),
            "volume": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Volume",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(DocrunticketsForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class DocwellheadpressuresForm(ModelForm):
    class Meta:
        model = Docwellheadpressures
        fields = [
            "userid",
            "productionptid",
            "docdate",
            "tubingpressure",
            "casingpressure",
            "chokesize",
            "stamp",
            "notes",
            "inputbyid",
            "docsourcecode",
            "api",
        ]

        # Add other widgets here as needed
        widgets = {
            "userid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The User ID",
                }
            ),
            "productionptid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Productionpt ID",
                }
            ),
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "tubingpressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Tubing Pressure",
                }
            ),
            "casingpressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Casing Pressure",
                }
            ),
            "chokesize": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Choke Size",
                }
            ),
            "stamp": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Stamp"}
            ),
            "notes": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Notes"}
            ),
            "inputbyid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Input By ID",
                }
            ),
            "docsourcecode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Doc Source Code",
                }
            ),
            "api": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The API"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(DocrunticketsForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class DocwaterdispositionForm(ModelForm):
    class Meta:
        model = Docwaterdisposition
        fields = [
            "userid",
            "tankid",
            "docdate",
            "volume",
            "reasoncode",
            "startlevel",
            "endlevel",
            "onseal",
            "offseal",
            "valvetypeid",
            "disposalsiteid",
            "transporterid",
            "stamp",
            "notes",
            "inputbyid",
            "docsourcecode",
            "noru",
            "new",
        ]

        # Add other widgets here as needed
        widgets = {
            "userid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The User ID",
                }
            ),
            "tankid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Tank ID",
                }
            ),
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "volume": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Volume",
                }
            ),
            "reasoncode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Reason Code",
                }
            ),
            "startlevel": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Start Level",
                }
            ),
            "endlevel": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The End Level",
                }
            ),
            "onseal": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The On Seal",
                }
            ),
            "offseal": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Off Seal",
                }
            ),
            "valvetypeid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Valve Type ID",
                }
            ),
            "disposalsiteid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Disposal Site ID",
                }
            ),
            "transporterid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Transporter ID",
                }
            ),
            "stamp": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Stamp"}
            ),
            "notes": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Notes"}
            ),
            "inputbyid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Input By ID",
                }
            ),
            "docsourcecode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Doc Source Code",
                }
            ),
            "noru": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Noru"}
            ),
            "new": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The New"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(DocwaterdispositionForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class DocwelltestsForm(ModelForm):
    class Meta:
        model = Docwelltests
        fields = [
            "userid",
            "docdate",
            "wellsiteid",
            "entityid",
            "entitytypeid",
            "hourson",
            "runtimeperc",
            "chokesize",
            "notforallocation",
            "testmethod",
            "oil",
            "gas",
            "water",
            "stamp",
            "notes",
            "inputbyid",
            "docsourcecode",
            "noru",
        ]

        # Add other widgets here as needed
        widgets = {
            "userid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The User ID",
                }
            ),
            "docdate": forms.SelectDateWidget(attrs={"class": "form-control mb-3"}),
            "wellsiteid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Well Site ID",
                }
            ),
            "entityid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Entity ID",
                }
            ),
            "entitytypeid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Entity Type ID",
                }
            ),
            "hourson": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Hourson",
                }
            ),
            "runtimeperc": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Run Time Perc",
                }
            ),
            "chokesize": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Choke Size",
                }
            ),
            "notforallocation": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Not Foral Location",
                }
            ),
            "testmethod": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Test Method",
                }
            ),
            "oil": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Oil"}
            ),
            "gas": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Gas"}
            ),
            "water": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Water"}
            ),
            "stamp": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Stamp"}
            ),
            "notes": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Notes"}
            ),
            "inputbyid": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Input By ID",
                }
            ),
            "docsourcecode": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter The Doc Source Code",
                }
            ),
            "noru": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter The Noru"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(DocwelltestsForm, self).__init__(*args, **kwargs)
        # Set the default value for 'docdate' to today's date
        self.fields["docdate"].initial = datetime.date.today()


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = [
            "tag_name",
            "parent_tag",
            "device",
            "data_type",
            "units",
            "description",
            "modbus_address",
            "modbus_function_code",
            "modbus_data_type",
            "modbus_unit_identifier",
            "modbus_tcp_ip",
            "modbus_baud_rate",
            "modbus_data_bits",
            "modbus_stop_bits",
            "modbus_parity",
        ]
        widgets = {
            "tag_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter Tag Name"}
            ),
            "parent_tag": forms.Select(attrs={"class": "form-control"}),
            "device": forms.Select(attrs={"class": "form-control"}),
            "data_type": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter Data Type"}
            ),
            "units": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Please Enter Units"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Description",
                }
            ),
            "modbus_address": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Address",
                }
            ),
            "modbus_function_code": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Function Code",
                }
            ),
            "modbus_data_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Data Type",
                }
            ),
            "modbus_unit_identifier": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Unit Identifier",
                }
            ),
            "modbus_baud_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Baud Rate",
                }
            ),
            "modbus_data_bits": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Data Bits",
                }
            ),
            "modbus_stop_bits": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Stop Bits",
                }
            ),
            "modbus_parity": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modbus Parity",
                }
            ),
        }

    # def __init__(self, *args, **kwargs):
    #     super(TagForm, self).__init__(*args, **kwargs)
    #     # Fetch data from device_list view and populate the device field choices
    #     request = kwargs.get('request')
    #     print(f"==>> request: {request}")
    #     devices_response = device_list(request=request)
    #     if devices_response.status_code == 200:
    #         devices_data = devices_response.data
    #         device_choices = [(device['id'], device['device_name']) for device in devices_data]
    #         self.fields['device'].choices = device_choices
    #     else:
    #         # Fallback if unable to fetch data
    #         self.fields['device'].queryset = device.objects.all()

    #     # Fetch data from tag_list view and populate the parent_tag field choices
    #     tags_response = tag_list(request=None)
    #     if tags_response.status_code == 200:
    #         tags_data = tags_response.data
    #         tag_choices = [(tag['id'], tag['tag_name']) for tag in tags_data]
    #         self.fields['parent_tag'].choices = tag_choices
    #     else:
    #         # Fallback if unable to fetch data
    #         self.fields['parent_tag'].queryset = Tag.objects.all()


class ModemForm(forms.ModelForm):
    # related_modem = forms.ModelChoiceField(queryset=modem.objects.none(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = modem
        fields = ["name", "iccid"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modem Name",
                }
            ),
            "iccid": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please Enter Modem ICCID",
                }
            ),
        }

    """def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super(ModemForm, self).__init__(*args, **kwargs)
        if queryset is None:
            self.fields['related_modem'].queryset = modem.objects.all()
        else:
            self.fields['related_modem'].queryset = queryset
    """


class DeviceForm(forms.ModelForm):
    class Meta:
        model = device
        fields = [
            "device_name",
            "device_id",
            "unit_slave",
            "plc_type",
            "station",
            "station_location",
            "baud_rate",
            "run_status",
        ]
        widgets = {
            "device_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "deviceNameFormControlInput1",
                    "placeholder": "Please Enter Device Name",
                }
            ),
            "device_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "deviceIdFormControlInput1",
                    "placeholder": "Please Enter Device ID",
                }
            ),
            "unit_slave": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "unitSlave",
                    "placeholder": "Please Enter Unit Slave",
                }
            ),
            "plc_type": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "plcType",
                    "placeholder": "Please Enter Plc Type",
                }
            ),
            "station": forms.Select(attrs={"class": "form-control", "id": "station"}),
            "station_location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "stationLocation",
                    "placeholder": "Please Enter Station Location",
                }
            ),
            "baud_rate": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "baudRate",
                    "placeholder": "Please Enter Baud Rate",
                }
            ),
            "run_status": forms.CheckboxInput(
                attrs={"class": "custom-control-input", "id": "runStatus"}
            ),
        }


class DeviceInputForm(forms.ModelForm):
    class Meta:
        model = Device_inputs
        fields = [
            "name",
            "current_production",
            "hour_production_limit",
            "k_factor",
            "kill_switch",
            "low_line_pressure",
            "max_output",
            "max_pressure",
            "min_output",
            "min_pressure",
            "output_channel",
            "start",
            "start_casing_pressure",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "NameFormControlInput",
                    "placeholder": "Please Enter Name",
                }
            ),
            "current_production": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "CurrentProductionFormControlInput",
                    "placeholder": "Please Enter Current Production",
                }
            ),
            "hour_production_limit": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "HourProductionLimit",
                    "placeholder": "Please Enter Hour Production Limit",
                }
            ),
            "k_factor": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "KFactor",
                    "placeholder": "Please Enter K. Factor",
                }
            ),
            "kill_switch": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "KillSwitch",
                    "placeholder": "Please Enter Kill Switch",
                }
            ),
            "low_line_pressure": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "LowLinePressure",
                    "placeholder": "Please Enter Low Line Pressure",
                }
            ),
            "max_output": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "MaxOutput",
                    "placeholder": "Please Enter Max Output",
                }
            ),
            "max_pressure": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "MaxPressure",
                    "placeholder": "Please Enter Max Pressure",
                }
            ),
            "min_output": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "MinOutput",
                    "placeholder": "Please Enter Min Output",
                }
            ),
            "min_pressure": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "MinPressure",
                    "placeholder": "Please Enter Min Pressure",
                }
            ),
            "output_channel": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "OutputChannel",
                    "placeholder": "Please Enter Output Channel",
                }
            ),
            "start": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "start",
                    "placeholder": "Please Enter Start",
                }
            ),
            "start_casing_pressure": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "StartCasingPressure",
                    "placeholder": "Please Enter Start Casing Pressure",
                }
            ),
        }


class CustomBaseModelFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(CustomBaseModelFormSet, self).__init__(*args, **kwargs)
        if self.extra_forms:
            # Set the initial value for the date field of the last form (the extra form)
            self.extra_forms[-1].initial["date_field"] = timezone.localdate()


class DynamicQueryForm(forms.Form):
    location = forms.CharField(required=False)
    date_max = forms.DateField(required=False)
    # Add more fields as needed


"""# forms.py
from django import forms
from django.forms import modelformset_factory, BaseModelFormSet
from django.utils import timezone
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['date_field', 'other_field']

class CustomBaseModelFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(CustomBaseModelFormSet, self).__init__(*args, **kwargs)
        if self.extra_forms:
            self.extra_forms[-1].initial['date_field'] = timezone.localdate()

MyModelFormSet = modelformset_factory(
    MyModel,
    form=MyModelForm,
    formset=CustomBaseModelFormSet,
    extra=1
)
"""
