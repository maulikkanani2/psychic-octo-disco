from rest_framework import serializers
from finance_app.models import Trans
from bi_app.models import modem, device, Tag

class TransSerializer(serializers.ModelSerializer):
    gen_acc = serializers.IntegerField()
    Period = serializers.DateTimeField()
    Amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    Qty = serializers.DecimalField(max_digits=10, decimal_places=2)
    Account_name = serializers.CharField()
    Gen_account = serializers.CharField()
    LOS_aggregation = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        model = Trans
        fields = ['gen_acc', 'Period', 'Amount', 'Qty', 'Account_name', 'Gen_account', 'gen_acc', 'LOS_aggregation',
                  'total_amount']

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        # Convert Amount to float if it's not None
        if rep.get('Amount') is not None:
            rep['Amount'] = float(rep['Amount'])

        # Convert Qty to float if it's not None
        if rep.get('Qty') is not None:
            rep['Qty'] = float(rep['Qty'])

        # Convert total_amount to float if it's not None
        if rep.get('total_amount') is not None:
            rep['total_amount'] = float(rep['total_amount'])

        # Convert LOS_aggregation to float if it's not None
        if rep.get('LOS_aggregation') is not None:
            rep['LOS_aggregation'] = float(rep['LOS_aggregation'])

        return rep
class ModemSerializer(serializers.ModelSerializer):
    class Meta:
        model = modem
        fields = ['name', 'iccid']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = ['id', 'device_name', 'device_id', 'unit_slave', 'plc_type', 'station',
                  'station_location', 'run_status']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name', 'parent_tag', 'device', 'data_type', 'units', 'description', 'modbus_address',
                  'modbus_function_code', 'modbus_data_type', 'modbus_unit_identifier', 'modbus_tcp_ip',
                  'modbus_baud_rate', 'modbus_data_bits', 'modbus_stop_bits', 'modbus_parity']