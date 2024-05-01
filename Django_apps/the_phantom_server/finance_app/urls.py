from django.urls import path, include
import debug_toolbar
from .views import financialview
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('exports', views.exports_data, basename='exports')
urlpatterns = router.urls

urlpatterns += [

    path("financials",views.financialview , name="Financials"),
    path("loe_analytics", views.loe_analytics, name="loe_analytics_view"),
    path("spend_analysis", views.spend_analysis, name="spend_analysis_view"),
    #path("loe", views.gas_meter, name="loe"),
    #path("chemical", views.all_gas, name="chemical"),
]
