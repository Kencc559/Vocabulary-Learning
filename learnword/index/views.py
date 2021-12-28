#file: index/views.py

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.



def index(request):
    if request.method == "GET":
        if (not hasattr(request, 'session')) or ('user' not in request.session):
            return render(request, "index.html")
        index = {
            'login': 'ok',
            'infor': request.session['user']['username'],
        }
        return render(request, "index.html", locals())

    elif request.method == "POST":
        searchword = request.POST.get('searchWord','0')
        print(searchword)
        return HttpResponse('searchword: '+ searchword)


