#file: vocabs/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from users.models import User
from . import models

# Create your views here.

def check_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/t1/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/t1/user/login')
        return fn(request, *args, **kwargs)
    return wrap

@check_login
def review(request):
    print("review")
    return render(request, "review_list.html")

@check_login
def reviewword(request):
    print("reviewword")

    return render(request, "review_word.html")

@check_login
def learn_eng_website_list(request):
    uid = request.session['user']['id']
    if request.method == 'GET':
        # auser = User.objects.get(id=uid)
        # webs = auser.learningweb_set.all()
        webs = models.Learningweb.objects.filter(user = uid)
        return render(request, "learn_eng_website_list.html",locals())
    elif request.method == 'POST':
        auser = User.objects.get(id=uid)
        webname = request.POST.get('web_name','')
        webaddr = request.POST.get('web_addr','')
        aweb = models.Learningweb.objects.create(webname=webname, webaddr=webaddr, user=auser)
        webs = auser.learningweb_set.all()
        return render(request, "learn_eng_website_list.html", locals())


