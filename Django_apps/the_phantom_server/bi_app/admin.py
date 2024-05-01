from django.contrib import admin
from .models import Docgasmeterreadings, flow_controller_data
#Register your models here.
admin.site.register(Docgasmeterreadings)
admin.site.register(flow_controller_data)
