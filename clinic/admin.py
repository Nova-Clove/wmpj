from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Clinic
# Register your models here.

class ClinicAdmin(admin.ModelAdmin):
    list_display = ['patient_name','patient_phone','patient_address','patient_case','drug','fees','datetime','doctor']
    list_filter = ['patient_address','patient_case','drug','fees','datetime','doctor']
    search_fields = ['patient_name','patient_id']

admin.site.register(Clinic, ClinicAdmin)