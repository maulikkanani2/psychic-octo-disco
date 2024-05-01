import django_filters
from django import forms
from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import OilLedger, flow_controller_data, device

class OilLedgerFilter(django_filters.FilterSet):
    docdatedate = DateFilter(
        field_name='docdatedate',
        lookup_expr='exact',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    tankid__cal_id__name = DateFilter(
        field_name='name',
        lookup_expr='exact',
        widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control'}),
    )
    class Meta:
        model = OilLedger
        fields = ['docdatedate','tankid__cal_id__name'] #date and location name (related)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Rename foreign key fields as needed
        self.filters['tankid__cal_id__name'].label = 'Location'
        #self.filters['tankid__tankname'].label = 'Tank Name'
        
        
class FlowControllerDataFilter(django_filters.FilterSet):
    timestamp = DateFilter(
        field_name='timestamp__date',
        lookup_expr='exact',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
    )
    device__device_name = ModelChoiceFilter(
        field_name='device',
        queryset=device.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Device Name'
    )
    class Meta:
        model = flow_controller_data
        fields = ['timestamp', 'device__device_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.filters['device__device_name'].label = 'Device Name'
        self.filters['timestamp'].label = 'Timestamp'
