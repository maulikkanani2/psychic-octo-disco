from celery import shared_task
from celery.schedules import crontab
from django.conf import settings
import requests
import json
import datetime
from zip_file_script.zip_script import StoreData
from django.db import connections
# from .models import store_zip_file
from datetime import datetime
from django_descope.models import DescopeUser


@shared_task
def print_hello():
    print("Hello, world!")
    return "task is completed!"

# @shared_task
# def store_zip_file_data(username, file_id, file_path):
#     user = DescopeUser.objects.using('default').get(username=username)
#     store_zip_data = store_zip_file.objects.using('third_db').filter(user=user).get(file_id=file_id)
#     if store_zip_data.is_process:
#         cursor = connections['third_db'].cursor()    
#         store_data_obj = StoreData(cursor, file_path)
#         store_data_obj.create_dbf_table()
#         store_data_obj.create_shp_table()
#         store_data_obj.extract_data()
#         store_data_obj.remove_exist_folder()
#         store_zip_data.is_process = False
#         store_zip_data.is_complete = True
#         store_zip_data.completed_at = datetime.now()
#         store_zip_data.save()
#         return "Data has been store successfully!"
#     if store_zip_data.is_complete:
#         return "Data has been already stored in database!"
    
    
    
    