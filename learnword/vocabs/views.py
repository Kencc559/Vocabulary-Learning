#file: vocabs/views.py

from django.shortcuts import render
from django.http import HttpResponseRedirect

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
    return render(request, "learn_eng_website_list.html")