#file: users/views.py
import hashlib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
import re
# Create your views here.

def registor(request):
    if request.method == 'GET':
        return render(request, "user/register.html")
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password1 = request.POST.get('password1','')
        password2 = request.POST.get('password2','')

        if len(username) < 8:
            username_error = '用戶名太短!至少8碼'
            return render(request, "user/register.html", locals())
        result = re.findall('[\d*\w*]',username)
        if len(result) != len(username):
            username_error = '勿有特殊符號.須用字母及數字'
            return render(request, "user/register.html", locals())
        if len(password1) == 0:
            password1_error = '密碼不能為空'
            return render(request, "user/register.html", locals())
        if password1 != password2:
            password2_error = '驗證密碼錯誤'
            return render(request, "user/register.html", locals())

        m = hashlib.md5()
        password1 += 'salt'
        m.update(password1.encode())

    try:
        auser = models.User.objects.get(username=username)
        username_error = '已存在用戶名' + auser.username
        return render(request, "user/register.html", locals())

    except:
        auser = models.User.objects.create(username=username, password=m.hexdigest())
        reg_ok = '註冊成功!請'
        resp = render(request, 'user/login.html', locals())
        resp.set_cookie('username',username)

        return resp


def login(request):
    if request.method == 'GET':
        username = request.COOKIES.get('username','')
        return render(request, "user/login.html", locals())
    elif request.method == "POST":
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')

        if username == "":
            username_error = '用戶名不可為空 !!'
            return render(request, "user/login.html", locals())
        elif password == "":
            password_error = '密碼不可為空 !!'
            return render(request, "user/login.html", locals())
        password += 'salt'
        m = hashlib.md5()
        m.update(password.encode())
        try:
            auser = models.User.objects.get(username=username, password=m.hexdigest())
            request.session['user'] = {
                'username' : username,
                'id' : auser.id
            }
            index = {
                'login': 'ok',
                'infor': request.session['user']['username'],
            }

            resp = render(request, 'index.html', locals())
            resp.set_cookie('username',username)
            return resp
        except:
            password_error = "用戶名或密碼不正確"
            return render(request, "user/login.html", locals())

        # login_ok = '成功'
        # return render(request, "user/login.html", locals())
        # return HttpResponse("login OK !")



def logout(request):
    if 'user' in request.session:
        del request.session['user']
        return HttpResponseRedirect('/t1/user/login')

def infor(request):
    username = request.COOKIES.get('username', '')
    if request.method == 'GET':
        return render(request, "user/infor.html", locals())

    elif request.method == 'POST':
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if len(password1) == 0:
            password1_error = '密碼不能為空'
            return render(request, "user/infor.html", locals())
        if password1 != password2:
            password2_error = '驗證密碼錯誤'
            return render(request, "user/infor.html", locals())
    m = hashlib.md5()
    password1 += 'salt'
    m.update(password1.encode())
    try:
        auser = models.User.objects.get(username=username)
        auser.password = m.hexdigest()
        auser.save()
        password2_error = '修改成功 !!'

    except:
        username = '無此帳號!!'
    return render(request, 'user/infor.html', locals())



