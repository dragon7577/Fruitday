from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add/$',add_cart,name='add'),
    url(r'^buy/$',buy_cart,name='buy'),
    url(r'^delete/$',delete_cart,name='delete'),
]