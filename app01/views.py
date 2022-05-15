from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app01 import models
import json


# Create your views here.


# 登录
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        # 验证用户名密码是否正确，然后登陆存入session

        uid = request.POST.get("uid")
        pwd = request.POST.get("pwd")
        print(type, uid, pwd)
        if len(models.User.objects.filter(username=uid, password=pwd)) != 0:
            # 登录成功

            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        models.User.objects.create(username=username, password=pwd)
        return redirect("/user/register")


def admin_home(request):
    if request.method == 'GET':
        list = models.User.objects.all()
        return render(request, 'admin_home.html', {'topics': list})


def user_delete(request):
    id = request.GET.get('id')
    models.User.objects.filter(id=id).delete()
    return redirect("/admin/home/")
