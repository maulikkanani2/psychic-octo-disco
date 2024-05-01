from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime
from finance_app.models import Trans, Coa, Cc, Name, Voucher, CoaGen
from datetime import datetime
from unittest.mock import patch
from rest_framework.test import APITestCase
from bi_app.models import modem, Tag, device
from API.serializers import TransSerializer, ModemSerializer, TagSerializer,DeviceSerializer
from .views import create_modem, create_tag, tag_list
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory

class TransViewTestCase(TestCase):
    databases=['secondary']
    
    def setUp(self):
        self.client = APIClient()
            

    def test_trans_view(self):
        
        coa=Coa.objects.create(
            u2_id='194*1345-JE-3',
            category='AC',
            name='TEMP CASH',
            normal_bal='D',
            sl_req='SYS',
            sub_co='010',
            time_stamp=datetime.now(),
            u2_checksum='tfNCoo8OS2iOglOg5er7If==L'
        )
        
        cc = Cc.objects.create(
            u2_id='1',
            name="HAYS GU GENERAL FACILITY",
            time_stamp=datetime.now()
        )
        
        name = Name.objects.create(
            u2_id='1',
            address1="285 COUNTY ROAD 166",
            city="LONG BRANCH",
            country="US",
        )
        
        voucher = Voucher.objects.create(
            u2_id = '154*1345-JE-3',
            appr="SHG",
            appr_date=datetime.now(),
            company='420',
            time_stamp=datetime.now(),
        )
        
        coa_gen = CoaGen.objects.create(
            u2_id=1,
            acct_designation="GEOL",
            category= "AP",
            name= "GEOLOGICAL AND GEOPHYSICAL (G&G)",
            normal_bal= "D",
            sl_req= "SYS",
            time_stamp=datetime.now(),
        )
        
        trans = Trans.objects.create(
            u2_id='1',
            acct = coa,
            acctg_period= datetime.now(),
            activity_date= datetime.now(),
            amt= -6.58,
            app= "JB2325",
            company= "127",
            cost_center= cc,
            name=name,
            curr_status= "1",
            description= "Type 2 - Billed to outsiders",
            desc_txt= "Type 2 - Billed to outsiders",
            dist_company= "127",
            gen_acct= "11934643",
            gl_date= "20344 57232",
            stat1_amt= 34.71,
            stat1_qty1= 0.0,
            int_amt= -6.58,
            post_date= datetime.now(),
            post_time= "03:53PM",
            source_currency= "US",
            source_port= "pts_35@3",
            source_table= "TRANS",
            system_date= datetime.now(),
            system_time= "03:52PM",
            system_user_id= "OHW",
            type= "JB2",
            voucher= voucher,
            time_stamp= datetime.now(),
            gen_acc= coa_gen,
        )
        
        url = reverse('trans')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_trans_view_with_bad_request(self):
        url = reverse('trans')
        invalid_url = url + 'invalid_path/'

        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class ModemViewTestCase(APITestCase):
        
    @patch('bi_app.views.modem.objects.all')
    def test_modem_list(self, mock_modems_all):
        
        mock_modems = [
            modem(name='Mock Modem 1', iccid='iccid1'),
            modem(name='Mock Modem 2', iccid='iccid1')
        ]
        mock_modems_all.return_value = mock_modems
        
        url = reverse('modem_list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        serializer_data = ModemSerializer(mock_modems, many=True).data
        self.assertEqual(response.data, serializer_data)
 
class CreateModemTest(TestCase):
    
    @patch('bi_app.views.modem.objects.all')
    def test_create_modem_success(self, mock_modems_all):
        mock_modems = {
           'name': 'Mock Modem', 'iccid': 'iccid1'
        }
        mock_modems_all.return_value = mock_modems
        response = self.client.post(reverse('create_modem'), data=mock_modems)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len([response.data]), 1)
        self.assertEqual(response.data, mock_modems)
        
    @patch('bi_app.views.modem.objects.all')
    def test_create_modem_invalid_data(self, mock_modems_all):
        mock_modems = {}
        mock_modems_all.return_value = mock_modems
        response = self.client.post(reverse('create_modem'), data=mock_modems)
        error_message = response.data
        error_detail_of_name = error_message.get('name')[0]
        error_detail_of_iccid = error_message.get('iccid')[0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_detail_of_name, 'This field is required.')
        self.assertEqual(error_detail_of_iccid, 'This field is required.')
        
    @patch('bi_app.views.modem.objects.all')
    def test_create_modem_missing_fields(self, mock_modems_all):
        mock_modems = {
            'name': 'Mock Modem', 'iccid': ''
        }
        mock_modems_all.return_value = mock_modems
        response = self.client.post(reverse('create_modem'), data=mock_modems)
        errors = response.data.get('iccid')[0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('This field may not be blank.', errors)
        
    def test_create_modem_incorrect_method(self):
        response = self.client.get(reverse('create_modem'))
        errors = response.data.get('detail')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(errors, 'Method "GET" not allowed.')
        
class CreateTagTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        
        self.mock_modem = modem.objects.create(name="test modem", iccid="iccid1")
        self.mock_device = device.objects.create(
            device_name="Test Device",
            device_id="ABC123",
            unit_slave="1",
            plc_type="Siemens S7-1200",
            station=self.mock_modem,
            station_location="Building 1",
            baud_rate=9600,
            run_status=False
        )

    @patch('API.views.create_tag')
    def test_create_tag_success(self, mock_create_tag):
        mock_create_tag.return_value = Response(status=status.HTTP_201_CREATED)
        
        mock_data = {
            "tag_name": "Temperature",
            "device": self.mock_device.id,
            "data_type": "float",
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_address": 100,
            "modbus_function_code": 3,
            "modbus_data_type": "this is test modbus data type"
        }

        request = self.factory.post(reverse('create_tag'), mock_data, format='json')
        response = create_tag(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @patch('API.views.create_tag')
    def test_create_tag_with_serializer(self, mock_create_tag):
        
        mock_data = {
            "tag_name": "Temperature",
            "device": self.mock_device.id,
            "data_type": "float",
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_address": 100,
            "modbus_function_code": 3,
            "modbus_data_type": "this is test modbus data type"
        }
        mock_create_tag.return_value = mock_data
        

        serializer = TagSerializer(data=mock_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        self.assertEqual(Tag.objects.count(), 1)  
        
    @patch('API.views.create_tag')
    def test_create_tag_invalid_data(self, mock_create_tag):
        mock_data = {
            "tag_name": "",
            "device": self.mock_device.id,
            "data_type": "float",
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_address": 100,
            "modbus_function_code": 3,
        }
        mock_create_tag.return_value = mock_data

        request = self.factory.post(reverse('create_tag'), mock_data, format='json')
        response = create_tag(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('tag_name', response.data)
        self.assertIn('modbus_data_type', response.data)
       
    @patch('API.views.create_tag') 
    def test_create_tag_with_invalid_serializer(self, mock_create_tag):
        mock_data = {}
        mock_create_tag.return_value = mock_data
        serializer = TagSerializer(data=mock_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(Tag.objects.count(), 0)
     
    @patch('API.views.create_tag')
    def test_create_tag_missing_required_field(self, mock_create_tag):
        mock_data = {
            "tag_name": "Temperature",
            "device": self.mock_device.id,
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_function_code": 3,
        }
        mock_create_tag.return_value = mock_data

        request = self.factory.post(reverse('create_tag'), mock_data, format='json')
        response = create_tag(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('data_type', response.data)   
        self.assertIn('modbus_address', response.data)   
        self.assertIn('modbus_data_type', response.data)   
        
    @patch('API.views.create_tag')
    def test_create_tag_incorrect_method(self, mock_create_tag):
        mock_create_tag.return_value = Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        request = self.factory.get(reverse('create_tag'))
        response = create_tag(request)
        errors = response.data.get('detail')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        self.assertEqual(errors, 'Method "GET" not allowed.')
        
class TagListTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
         
    @patch('API.views.tag_list') 
    @patch('bi_app.views.Tag.objects.all')
    def test_get_tag_list_success(self, mock_tags_all, mock_create_tag):
        mock_create_tag.return_value = Response(status=status.HTTP_200_OK)
        mock_modem = modem(name="test modem", iccid="iccid1")
        mock_device = device(
            device_name="Test Device",
            device_id="ABC123",
            unit_slave="1",
            plc_type="Siemens S7-1200",
            station=mock_modem,
            station_location="Building 1",
            baud_rate=9600,
            run_status=False
        )
        mock_data_1 = {
            "tag_name": "Temperature1",
            "device": mock_device.id,
            "data_type": "float",
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_address": 100,
            "modbus_function_code": 3,
            "modbus_data_type": "this is test modbus data type"
        }
        mock_data_2 = {
            "tag_name": "Temperature2",
            "device": mock_device.id,
            "data_type": "float",
            "units": "°C",
            "description": "Temperature sensor reading",
            "modbus_address": 100,
            "modbus_function_code": 3,
            "modbus_data_type": "this is test modbus data type"
        }
        mock_tags = [
            Tag(**mock_data_1),
            Tag(**mock_data_2)
        ]
        mock_tags_all.return_value = mock_tags
        request = self.factory.get(reverse('tag_list'))
        response = tag_list(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


