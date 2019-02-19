from django.contrib import admin
from .models import *

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_No','receiver_name','receiver_phone','receiver_address','create_time','update_time']
    list_display_links = ['order_No']
    list_editable = ['receiver_name','receiver_phone','receiver_address']

admin.site.register(Order,OrderAdmin)