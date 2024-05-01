from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import F, Sum
from django.db.models.functions import TruncMonth, Round
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from finance_app.models import Trans
from bi_app.models import modem, Tag, device
from API.serializers import TransSerializer, ModemSerializer, TagSerializer,DeviceSerializer

@api_view(['GET'])
def transdata(request):
    #try:
    # Print request parameters for debugging
        print("Request GET parameters:", request.GET)
        filter_months = request.GET.get('range')
        months = int(filter_months) if filter_months != 'Range' and filter_months is not None else 8
        months_ago = datetime.now() - relativedelta(months=months)

        filter_period = request.GET.get('period')
        period = filter_period if filter_period != 'Period Type' and filter_period is not None else 'acctg_period'
        gross_gen_acc = [410, 415, 420, 430, 440, 450, 470, 481, 490, 510, 515, 800, 811, 820, 830, 840, 850, 860, 870,
                        875,
                        880, 881, 883, 888, 882, 884, 885]
        gross_columns = ['acct__name', period, 'stat1_amt', 'stat1_qty1', 'gen_acc','gen_acc__name']
        net_gen_acc = [150,159,151,152,153,154,156,155,157,158,410, 415, 420, 430, 440, 450, 470, 481,
                490,510,515,520,525,530,540]
        net_columns = ['acct__name', period, 'AMT', 'QTY1', 'gen_acc']
        request_type = "gross"
        if request_type == "gross":
            gen_acc_code = gross_gen_acc
            cols = gross_columns
            amount = 'stat1_amt'
            qty = 'stat1_qty1'
        else:
            gen_acc_code = net_gen_acc
            cols = net_columns
            amount = 'AMT'
            qty = 'QTY1'

        queryset = Trans.objects.only(*cols) \
            .filter(**{"%s__gte" % period: months_ago, "gen_acc__in": gen_acc_code}) \
            .annotate(month=TruncMonth(period)) \
            .annotate(
            Period=F(period),
            Amount=Round(F(amount), 2),
            Qty=F(qty),
            Account_name=F('acct__name'),
            Gen_account=F('gen_acc__name'),
            LOS_aggregation=F('gen_acc__LOS_aggregation')
        ) \
            .values('Period', 'Amount', 'Qty', 'Account_name', 'Gen_account', 'gen_acc','LOS_aggregation') \
            .annotate(total_amount=Sum('Amount')) \
            .order_by('Period')


        # Print queryset data for debugging
        # print("Queryset:", list(queryset))

        # Serialize queryset data
        serializer = TransSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #except Exception as e:
    #    print(e)
    #    return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def modem_list(request):
    if request.method == 'GET':
        modems = modem.objects.all()
        serializer = ModemSerializer(modems, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_modem(request):
    if request.method == 'POST':
        serializer = ModemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_tag(request):
    if request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def device_list(request):
    if request.method == 'GET':
        devices = device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_device(request):
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
