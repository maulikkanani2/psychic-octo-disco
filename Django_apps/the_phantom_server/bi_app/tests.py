import json
from django.test import TestCase, Client
from django.test import RequestFactory
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from unittest import mock
from unittest.mock import patch
from datetime import date, datetime, timedelta
from .models import OilLedger, Locations, Eqptank, Ptsproductionpt, Sumdailyproduction
from bi_app.views import consolidated_production, oil_inventory


class OilInventoryViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.locations = Locations.objects.create(id=1, name="Surat")
        self.eqptank = Eqptank.objects.create(compid=1, tankname="Tank", cal_id=self.locations)
        OilLedger.objects.create(
            docdatedate=date.today(),
            tankid=self.eqptank,
            final_gauge=100,
            rtvolume=50,
            production=30,
        )

    def test_oil_inventory_view(self):
        response = self.client.get(reverse('oil_inventory_view'))
        context = response.context
        average_sales = context.get('average_sales')
        average_production = context.get('average_production')
        average_inventory = context.get('average_inventory')
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oil Inventory")
        self.assertIn("oil", response.context)
        self.assertEqual(average_sales, 50.0)
        self.assertEqual(average_production, 30.0)
        self.assertEqual(average_inventory, 100.0)
        self.assertIsNotNone(context.get("div_line_chart1"))
        self.assertIsNotNone(context.get("script_line_chart1"))
        self.assertIsNotNone(context.get("div_line_chart2"))
        self.assertIsNotNone(context.get("script_line_chart2"))
        self.assertIsNotNone(context.get("div_line_chart3"))
        self.assertIsNotNone(context.get("script_line_chart3"))

    def test_search_value_oil_inventory_view(self):
        response = self.client.get(
            reverse("oil_inventory_view")
            + f"?docdatedate={date.today()}&tankid__cal_id__name=Surat"
        )
        search_data = response.context.get("oil").first()
        context = response.context

        average_sales = context.get("average_sales")
        average_production = context.get("average_production")
        average_inventory = context.get("average_inventory")
        location = Locations.objects.all().first()
        eqptank = Eqptank.objects.all().first()
        oil_ledger = OilLedger.objects.filter(docdatedate=date.today()).first()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oil Inventory")
        self.assertIn("oil", response.context)
        self.assertEqual(average_sales, 50.0)
        self.assertEqual(average_production, 30.0)
        self.assertEqual(average_inventory, 100.0)
        self.assertEqual(location.name, search_data["tankid__cal_id__name"])
        self.assertEqual(eqptank.tankname, search_data["tankid__tankname"])
        self.assertEqual(str(date.today()), search_data["docdatedate"])
        self.assertEqual(oil_ledger.final_gauge, search_data["final_gauge"])
        self.assertEqual(oil_ledger.docdatedate, search_data["docdatedate"])
        self.assertEqual(oil_ledger.rtvolume, search_data["rtvolume"])
        self.assertEqual(oil_ledger.production, search_data["production"])
        self.assertEqual(
            oil_ledger.tankid.cal_id.name, search_data["tankid__cal_id__name"]
        )
        self.assertIsNotNone(context.get("div_line_chart1"))
        self.assertIsNotNone(context.get("script_line_chart1"))
        self.assertIsNotNone(context.get("div_line_chart2"))
        self.assertIsNotNone(context.get("script_line_chart2"))
        self.assertIsNotNone(context.get("div_line_chart3"))
        self.assertIsNotNone(context.get("script_line_chart3"))

    def test_search_inventory_with_invalid_date(self):
        response = self.client.get(
            reverse("oil_inventory_view")
            + f"?docdatedate={datetime.now()}&tankid__cal_id__name=Surat"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response._container[0].decode(),
            "Invalid format for docdatedate. Please use 'YYYY-MM-DD'.",
        )

class ConsolidatedProductionViewTestCase(TestCase):

    @classmethod
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.productionpt = Ptsproductionpt(productionptid=1)
        self.sumdailyproduction = Sumdailyproduction(
            id=161630,
            entityid=self.productionpt,
            docdate="2014-01-06 05:30:00+05:30",
            entitytype=4,
            oil=0.23999999463558197,
            water=4,
            gas=145.02000427246094,
        )

    @patch('bi_app.views.Ptsproductionpt.objects.all')
    @patch('bi_app.views.Sumdailyproduction.objects.filter')
    def test_consolidated_production_view(self, mock_sumdailyproduction_filter, mock_ptsproductionpt_all):
        mock_ptsproductionpt_all.return_value = self.productionpt
        mock_sumdailyproduction_filter.return_value = self.sumdailyproduction
        
        request = RequestFactory().get(reverse("cons_view"))
        request.user = self.user

        response = consolidated_production(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response, HttpResponse)

    @patch('bi_app.views.Ptsproductionpt.objects.all')
    @patch('bi_app.views.Sumdailyproduction.objects.filter')
    def test_consolidated_production_error_handling(self, mock_sumdailyproduction_filter, mock_ptsproductionpt_all):
        mock_ptsproductionpt_all.return_value = self.productionpt
        mock_sumdailyproduction_filter.return_value = self.sumdailyproduction

        request = RequestFactory().get(reverse("cons_view")+'?ptrid=99')
        request.user = self.user

        response = consolidated_production(request)
        self.assertEqual(response.status_code, 200)
