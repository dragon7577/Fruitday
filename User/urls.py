from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$',login_views,name='login'),
    url(r'^register/$',register_views,name='register'),
    url(r'^check_name/$',check_name,name='check'),
    url(r'^logout/$',logout_views,name='logout'),
    url(r'^login_checked/$',login_checked,name='login_checked'),
]