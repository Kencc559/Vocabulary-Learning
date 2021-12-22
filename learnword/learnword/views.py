
from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")



def register_view(request):
    return render(request, "register.html")

def review_list_view(request):
    return render(request, "review_list.html")

def learn_eng_website_list_view(request):
    return render(request, "learn_eng_website_list.html")

login_form_html = '''
<form action="/login" method="post">
    用戶名:<input name="username" type="text">
    密碼:<input name="pw" type="text">
    <input type="submit" value="登入">
</form>
'''