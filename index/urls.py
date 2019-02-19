from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views,name='index'),
    url(r'^hot/$', hot_views,name='hot'),
    url(r'^product/$', product_views,name='product'),
    url(r'^consult/$', consult_views,name='consult'),
    url(r'^touch/$', touch_views,name='touch'),
    url(r'^detail/$',detail_views,name='detail')

]