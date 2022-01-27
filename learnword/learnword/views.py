#file: learnword/views.py
import json
import pyrebase

from django.http import HttpResponse
from google.oauth2 import id_token
from google.auth.transport import requests
from django.shortcuts import render
from django.contrib import auth

GOOGLE_OAUTH2_CLIENT_ID = '702079640017-rva3kqr1ad3mm1780l7mrhfkabgqrc3c.apps.googleusercontent.com'
#
config = {
    'apiKey': "AIzaSyApeowhnlWPMVx0eOlYMOkCyvX9fFCYwdU",
    'authDomain': "kktest-a2705.firebaseapp.com",
    # 'databaseURL' : "https://kktest-a2705.firebaseapp.com",
    'databaseURL' : "https://kktest-a2705-default-rtdb.asia-southeast1.firebasedatabase.app/",
    'projectId': "kktest-a2705",
    'storageBucket': "kktest-a2705.appspot.com",
    'messagingSenderId': "60111880084",
    'appId': "1:60111880084:web:6738cbe26a49ad19205981"
}
 # Initialize Firebase
firebase = pyrebase.initialize_app(config)
auth2 = firebase.auth()
database = firebase.database()

def test(request):

    # return render(request, 'test_google.html')
    #

    if request.method == 'GET':
        google_oauth2_client_id = GOOGLE_OAUTH2_CLIENT_ID

        return render(request,'test_google.html',locals())
    elif request.method == 'POST':
        google_oauth2_client_id = GOOGLE_OAUTH2_CLIENT_ID
        print(request)
        print('*' * 50)

        token = request.json['id_token']
        print(token)
    #     id_token = {
    #         'id':'11',
    #         'name':'KKman',
    #     }

        try:
            id_info = id_token.verify_oauth2_token(
                # id_info = id_token.verify_*_token(
                token,
                requests.Request(),
                GOOGLE_OAUTH2_CLIENT_ID
            )
            print('*' * 20, id_info, '*' * 20)
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
        except ValueError:
            # Invalid token
            raise ValueError('Invalid token')

        print('登入成功')
        # return jsonify({}), 200
        return HttpResponse(json.dumps(id_token),content_type='application/json')

    else:
        return HttpResponse('test NG')






# @app.route('/google_sign_in', methods=['POST'])
# def google_sign_in():
#     print(request)
#     print('*' * 50)
#
#     token = request.json['id_token']
#     print(token)
#
#     try:
#         id_info = id_token.verify_oauth2_token(
#             # id_info = id_token.verify_*_token(
#             token,
#             requests.Request(),
#             GOOGLE_OAUTH2_CLIENT_ID
#         )
#         print('*' * 20, id_info, '*' * 20)
#         if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#             raise ValueError('Wrong issuer.')
#     except ValueError:
#         # Invalid token
#         raise ValueError('Invalid token')
#
#     print('登入成功')
#     return jsonify({}), 200

def postsign(request):
    email = request.POST.get('email')
    passw = request.POST.get('pass')
    try:
        user = auth2.sign_in_with_email_and_password(email,passw)
    except:
        message = 'Invalid credentials'
        return render(request, 'test_google.html',{'message':message})
    print(user)
    session_id = user['idToken']
    request.session['uid'] = session_id
    return render(request,'welcome.html',{'e':email})

def logout(request):
    auth.logout(request)
    print('logout')
    return render(request, 'test_google.html')

def signUp(request):
    print('signup')
    return render(request, 'signup.html')

def postsignup(request):
    print('posetsignup')
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('pass')

    user = auth2.create_user_with_email_and_password(email, passw)

    uid = user['localId']
    print(uid)

    data = {"name":name, "status": "1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request, 'test_google.html')
    # return HttpResponse('Create OK.')
'''
login_form_html = 
<form action="/login" method="post">
    用戶名:<input name="username" type="text">
    密碼:<input name="pw" type="text">
    <input type="submit" value="登入">
</form>
'''