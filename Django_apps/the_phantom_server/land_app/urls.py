from django.urls import path

from . import views

urlpatterns = [


    path("land_map", views.map_sqlview, name = 'map_view' ),
    # path("store_data", views.download_request, name="download_request"),
    #path("spend_analysis", views.spend_analysis, name="spend_analysis_view"),
    #path("loe", views.gas_meter, name="loe"),
    #path("chemical", views.all_gas, name="chemical"),
]
