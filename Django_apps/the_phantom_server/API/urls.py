from django.urls import path
from .views import *


urlpatterns = [
    path("v1/trans", transdata, name="trans"),
    path("v1/modem_list", modem_list, name="modem_list_api"),
    path("v1/create_modem", create_modem, name="create_modem_api"),
    path("v1/create_tag", create_tag, name="create_tag_api"),
    path("v1/tag_list", tag_list, name="tag_list_api"),
]