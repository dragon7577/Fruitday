from django.contrib.auth.hashers import check_password,make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *

import json
import logging


# Create your views here.
def login_views(request):
    if request.method == "GET":
        # 将请求源地址存进cookie
        url = request.META.get('HTTP_REFERER', '/')
        if 'uid' in request.session and 'uname' in request.session:
            return redirect(url)
        else:
            if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
                request.session['uid'] = request.COOKIES['uid']
                request.session['uname'] = request.COOKIES['uname']
                return redirect(url)
            else:
                return render(request, 'login.html')
    else:
        username = request.POST.get('uname')
        password = request.POST.get('upwd')
        user = User.objects.filter(username=username)
        if user:
            if check_password(password,user[0].password):
                request.session['uid'] = user[0].id
                request.session['uname'] = username
                resp = render(request,'index.html',{'username':username})
                if 'isSaved' in request.POST:
                    resp.set_cookie('uid',user[0].id)
                    resp.set_cookie('uname',username)
                return resp
            else:
                return redirect('/user/login/')
        else:
            return redirect('/user/login/')


def register_views(request):
    if request.method == "GET":
        return render(request,'register.html')
    else:
        username = request.POST.get('uname')
        upwd = request.POST.get('upwd')
        password = make_password(upwd,None,'pbkdf2_sha1')
        email = request.POST.get('uemail')
        phone = request.POST.get('uphone')
        try:
            user = User(username=username, password=password, email=email, phone=phone)
            user.save()
        except Exception as e:
            logging.warning(e)
        return render(request,'index.html',{'username':username})


def check_name(request):
    username = request.GET.get('uname')
    user = User.objects.filter(username=username)
    print(user)
    if user:
        dic = {
            'status':1,
            'msg':'用户名已经存在'
        }
    else:
        dic = {
            'status':0,
            'msg':'验证通过'
        }
    return HttpResponse(json.dumps(dic))


def logout_views(request):
    if 'uid' in request.session and 'uname' in request.session:
        del request.session['uid']
        del request.session['uname']
        #获取源地址
        url = request.META.get('HTTP_REFERER', '/')
        resp = redirect(url)
        # 判断cookies有则清除
        if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
            resp.delete_cookie('uid')
            resp.delete_cookie('uname')
        return resp
    return redirect('/')

def login_checked(request):
    if 'uid' in request.session and 'uname' in request.session:
        return render(request,'index.html',{'username':request.session['uname']})
    else:
        if 'uid' in request.COOKIES and 'uname' in request.COOKIES:
            request.session['uid'] = request.COOKIES['uid']
            request.session['uname'] = request.COOKIES['uname']
            return render(request,'index.html',{'username':request.COOKIES['uname']})
        else:
            return HttpResponse(None)