# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import Docpersonalinfo
import datetime
import random


def login(request):
    return render(request, 'userLoginin/login.html')


def startlogin(request):
    errors = []
    weizhi = request.POST.get('emailtel')
    password = request.POST.get('pwd')

    if not weizhi:
        errors.append('账号不能为空！')
    else:
        if not password:
            errors.append('密码不能为空！')
        else:
            if "@" in weizhi:
                bb = Docpersonalinfo.objects.get(useremail=weizhi)
                id = bb.userid
                user = auth.authenticate(username=id, password=password)
                if user:
                    auth.login(request, user)
                    return HttpResponseRedirect("/workregisterIndex/", {'bb': bb})
                else:
                    errors.append('账号或密码错误！')
            if weizhi.isdigit():
                bb = Docpersonalinfo.objects.get(usertel=weizhi)
                id = bb.userid
                user = auth.authenticate(username=id, password=password)
                if user:
                    auth.login(request, user)
                    return render_to_response("/workregisterIndex/", {'bb': bb})
                else:
                    errors.append('账号或密码错误！')
    return render_to_response("userLoginin/login.html", {'errors': errors})


def workregisterIndex(request):
    if not request.user.is_authenticated():
        return render_to_response("userLoginin/login.html")
    else:
        usernameGet = request.user
        bb = Docpersonalinfo.objects.get(userid=usernameGet)
        return render_to_response('workMzRegister/index.html', {'bb': bb})


def register(request):
    return render(request, 'userLoginin/register.html')


def startregister(request):
    userid = str(random.random())[2:18] + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = request.POST.get('email')
    password = request.POST.get('pwd1')
    realName = request.POST.get('realName')

    bb = Docpersonalinfo()
    bb.userid = userid
    bb.useremail = email
    bb.username = realName
    bb.save()

    user = User.objects.create_user(userid, email, password)
    user.is_active = True
    user.save

    return render_to_response('userLoginin/login.html')


def loginout(request):
    auth.logout(request)
    return render_to_response('userLoginin/login.html')
