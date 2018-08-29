# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from . import models
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# 自己的资料
from blog.models import Blogs


# 查看资料  还没加分页功能
def usercenter(request, name):
    # 查用户的信息
    user = User.objects.get(username=name)

    # 查询出该用户的博客
    blogs = Blogs.objects.filter(uname=name).order_by('-utime')

    # 该用户博客标签
    mark = {}
    for mk in blogs:
        if not mark.has_key(mk.marks_id):
            k = Blogs.objects.filter(uname=name, marks=mk.marks_id)

            mark[mk.marks_id] = len(k)
            # print "biaoqian=======", mk.marks_id, len(k), mark

    # return  HttpResponse()
    return render(request, 'center/usercenter.html', {'blogs': blogs, 'user': user, 'mark': mark})


# 登录
def uselogin(request):
    if request.method == 'GET':
        # 记住来源的url,如果没有则设置为首页('/blog')
        request.session['login_from'] = request.META.get('HTTP_REFERER', '/blog')
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 输入正确的账号，返回用户名，否则返回none
        user = authenticate(username=username, password=password)
        if user:
            print 66666666666, user
            login(request, user)
            # 重定向到来源的url
            return HttpResponseRedirect(request.session['login_from'])
            # return redirect('/blog/')
        else:
            return render(request, 'login.html', {'logs': '账号或密码错误！%s' % user})

    return render(request, 'login.html', {'logs': ' '})


# 修改密码
def set_pwd(request):
    if request.method == "POST":
        oldpassword = request.POST.get("oldpassword")
        newpassword = request.POST.get("newpassword")
        # 得到当前登录的用户，判断旧密码是不是和当前的密码一样
        username = request.user  # 打印的是当前登录的用户名
        user = User.objects.get(username=username)  # 查看用户
        ret = user.check_password(oldpassword)  # 检查密码是否正确
        if ret:
            user.set_password(newpassword)  # 如果正确就给设置一个新密码
            user.save()  # 保存
            return redirect("/login/")
        else:
            info = "输入的旧密码不正确"
            return render(request, "set_pwd.html", {"logs": info})
    return render(request, "set_pwd.html")


# 注册
def reg(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # password2 = request.POST.get("password2")
        email = request.POST.get("email")
        # first_name=request.POST.get("first_name")
        # last_name = request.POST.get("last_name")
        # if password1 != password2:
        #     return render(request, "blog/register.html", {'logs': '两次密码出入不一致'})
        name = User.objects.filter(username=username)
        # 如果用户存在，则name=1,不存在则name=0
        if name:
            return render(request, "register.html", {'message': '用户已存在%s' % len(name)})
        # else:
        # return render(request, "regist.html", {'logs': '用户bu存在%s' % len(name)})
        # 得到用户输入的用户名和密码创建一个新用户
        User.objects.create_user(username=username, password=password, email=email)

        # 注册成功后自动登录
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("/blog/")
    return render(request, "register.html")


# 注销
def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/blog/")
