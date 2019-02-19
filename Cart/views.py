import json
import logging
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Product.models import *
from .models import *

# Create your views here.
def add_cart(request):
    if 'uid' in request.session:
        user_id = request.session.get('uid')
        print(user_id)
    else:
        dict = {
            'status':0,
            'msg':'您还没有登录！'
        }
        return HttpResponse(json.dumps(dict))
    product_id = request.GET.get('product_id')
    quantity = request.GET.get('quantity')
    cart = Cart.objects.filter(product_id=product_id,user_id=user_id)
    if cart:
        #存在的话说明数据库中已经存在，更新
        cart[0].quantity = quantity
        cart[0].save()
    else:
        new_cart = Cart(user_id = user_id,product_id=product_id,quantity=quantity,checked=True)
        new_cart.save()
    dict = {
        'status':1,
        'msg':'添加成功'
    }
    return HttpResponse(json.dumps(dict))

def delete_cart(request):
    user_id = request.GET.get('user_id')
    product_id = request.GET.get('product_id')
    try:
        delcart = Cart.objects.filter(user_id=user_id,product_id=product_id)
        delcart.delete()
    except BaseException as e:
        logging.warning(e)
    return redirect('/cart/buy/')


def buy_cart(request):
    user_id = request.session.get('uid')
    carts = Cart.objects.filter(user_id=user_id)
    count = 0
    sumPrice = 0
    for cart in carts:
        count += cart.quantity
        sumPrice += cart.product.price
    return render(request,'cart.html',locals())