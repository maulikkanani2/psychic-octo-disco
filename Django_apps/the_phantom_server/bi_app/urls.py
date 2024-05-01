from django.urls import path
import debug_toolbar
from django.urls import include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('download', views.Download_data, basename='download')
urlpatterns = router.urls

urlpatterns += [
    path("", views.home, name="home"),
    path("pdf/", views.pdf, name="pdf"),
    path("gas_meter", views.gas_meter, name="gas_meter_input"),
    path("doc_compressor", views.doc_compressors, name="doc_compressor_input"),
    path("doc_run_tickets", views.doc_run_tickets, name="doc_run_tickets_input"),
    path("doc_water_disposition", views.doc_water_disposition, name="doc_water_disposition_input"),
    path("doc_well_tests", views.doc_well_tests, name="doc_well_tests_input"),
    path("all_gas", views.all_gas, name="gas_meter_view"),
    path("consolidated_production", views.consolidated_production, name="cons_view"),
    path("well_analysis", views.well_analysis, name="well_view"),
    path("production_analysis", views.production_analysis, name="production_analysis_view"),
    path("realtime", views.realtime, name="realtime_view"),
    path("oil_inventory", views.oil_inventory, name="oil_inventory_view"),
    path("reserves", views.reserves, name="reserves_view"),
    path("injection", views.injection, name="injection_view"),

    # Automation CRUD operations
    path("create_device", views.create_device, name="create_device"),
    path("update_device/<str:device_id>", views.update_device, name="update_device"),
    path("delete_device/<str:device_id>", views.delete_device, name="delete_device"),
    path("wellhead_automation", views.wellhead_automation, name="wellhead_automation"),
    # Modem CRUD oprations
    path("create_modem", views.create_modem, name="create_modem"),
    path("update_modem/<str:modem_id>", views.update_modem, name="update_modem"),
    path("delete_modem/<str:modem_id>", views.delete_modem, name="delete_modem"),
    
    #Device CRUD oprations

    #Tag CRUD oprations
    path("create_tag", views.create_tag, name="create_tag"),
    path("update_tag/<int:tag_id>", views.update_tag, name="update_tag"),
    path("delete_tag/<int:tag_id>", views.delete_tag, name="delete_tag"),
    
    # Device Input CRUD operations
    path("create_device_input", views.device_input_view, name="create_device_input"),
    path("update_device_input/<int:pk>", views.update_device_input, name="update_device_input"),
    path("delete_device_input/<int:pk>", views.delete_device_input, name="delete_device_input"),
    path("energy", views.energy, name="energy"),

    path('__debug__/', include(debug_toolbar.urls)),
]
