#file: learnword/views.py



login_form_html = '''
<form action="/login" method="post">
    用戶名:<input name="username" type="text">
    密碼:<input name="pw" type="text">
    <input type="submit" value="登入">
</form>
'''