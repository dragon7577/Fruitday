from django.shortcuts import render
from Product.models import *

# Create your views here.
def index_views(request):
    if 'uid' in request.session and 'uname' in request.session:
        username = request.session['uname']
    else:
        if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
            request.session['uid'] = request.COOKIES['uid']
            request.session['uname'] = request.COOKIES['uname']
            username = request.COOKIES['uname']
    cate = Category.objects.get(id=1)
    #3个小的banner
    Banners = cate.banner_set.filter(status=True)[0:3]
    productPics = cate.product_set.filter(status=True)[0:6]
    return render(request,'index.html',locals())

def hot_views(request):
    cate = Category.objects.get(id=2)
    productPics = cate.product_set.filter(status=True)[0:12]
    productPics2 = cate.product_set.filter(status=True)[12:]
    return render(request,'hot.html',locals())

def product_views(request):
    return render(request,'product.html')

def consult_views(request):
    return render(request,'consult.html')

def touch_views(request):
    return render(request,'touch.html')

def detail_views(request):
    id = request.GET.get('id')
    product = Product.objects.filter(id=id)[0]
    product_detail1 = product.detailpage_set.all()[0:4]
    product_detail2 = product.detailpage_set.all()[4:]
    return render(request,'detail.html',locals())