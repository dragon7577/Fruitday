from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone','create_time','update_time']
    list_display_links = ['username',]
    list_editable = ['email','phone']

admin.site.register(User,UserAdmin)

