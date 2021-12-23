#file: learnword/views.py

from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    return render(request, "index.html")


login_form_html = '''
<form action="/login" method="post">
    用戶名:<input name="username" type="text">
    密碼:<input name="pw" type="text">
    <input type="submit" value="登入">
</form>
'''