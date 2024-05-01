from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime
from .models import Trans, Coa, Cc, Name, Voucher, CoaGen
from datetime import datetime

class TransViewTestCase(TestCase):
    multi_db = True
    databases={'secondary'}
    
    def setUp(self):
        self.client = APIClient()
            
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

    def test_trans_view_with_bad_request(self):
        url = reverse('trans')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue('Error' in response.data)
