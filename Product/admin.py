from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','status','create_time','update_time']
    list_display_links = ['name']
    list_editable = ['status']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name','price','status','create_time','update_time']
    list_display_links = ['name']
    list_editable = ['price','status']
    list_filter = ['category']
    # fieldsets = (
    #     ('基本选项',{
    #         'fields':('name','price'),
    #     }),
    #     ('高级选项',{
    #         'fields':('image','status'),
    #         'classes':('collapse',)
    #     }),
    # )


class BannerAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    list_display_links = ['name']
    list_editable = ['status']


class DetailAdmin(admin.ModelAdmin):
    list_display = ['name','status']
    list_display_links = ['name']
    list_editable = ['status']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Banner,BannerAdmin)
admin.site.register(DetailPage,DetailAdmin)



