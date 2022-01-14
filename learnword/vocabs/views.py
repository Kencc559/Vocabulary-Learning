#file: vocabs/views.py
import datetime
import json
import os

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
    uid = request.session['user']['id']
    # word = request.POST.get('','')
    # print('uid= ',uid)
    try:
        auser = User.objects.get(id=uid)
        words = auser.vocab_set.all()
        dtn = datetime.datetime.now(datetime.timezone.utc)
        # print(dtn)
        for word in words:
            # print(word.vocab)
            ct = word.created_time
            # print(ct)
            dd = int((dtn - ct).days)+1
            word.delta = dd
            # print(word.delta)

        # dtn = datetime.datetime.strftime('%Y-%m-%d',dtn)
        # dt = datetime.datetime.strftime('%Y-%m-%d',dt)
        # dtn = datetime.datetime.strptime(dtn,'%Y-%m-%d %H:%M')
        # dt = datetime.datetime.strptime(dt,'%Y-%m-%d %H:%M')

        # print(dd)
        # print(type(dtn),dtn,"*"*20)
        # print(type(dt),dt,"*"*20)
    except Exception as e:
        print(e)
        err_msg = 'No data.'
        print('No data.')

    return render(request, "review_list.html", locals())

@check_login
def reviewword(request, **kwargs):
    print("reviewword")
    word = str(kwargs['word'])
    id = request.session['user']['id']
    print(word, id)
    try:
        aword = models.Vocab.objects.get(user_id=id, vocab=word)
        aword.review_cycle = int(aword.review_cycle) + 1
        aword.save()
        aword.chinese = json.loads(aword.chinese)
        aword.images = str(aword.image).split(',')
        aword.images1 = aword.images[:2]
        aword.images2 = aword.images[-2:]
        print(aword.images)
        print(type(aword.images))
        print(aword.chinese)
        print(type(aword.chinese))

    except Exception as e:
        print(e)
        err_msg = 'Not find any words.'

    # return render(request, "review_word.html", locals(),content_type='application/json')
    return render(request, "review_word.html", locals())
    # return HttpResponse(aword.chinese)

@check_login
def learn_eng_website_list(request):
    uid = request.session['user']['id']
    if request.method == 'GET':
        # auser = User.objects.get(id=uid)
        # webs = auser.learningweb_set.all()
        try:
            webs = models.Learningweb.objects.filter(user = uid)
        except Exception as e:
            print(e)
        return render(request, "learn_eng_website_list.html",locals())
    elif request.method == 'POST':
        auser = User.objects.get(id=uid)
        webname = request.POST.get('web_name','').strip("")
        webaddr = request.POST.get('web_addr','').strip("")
        if(( webname == '') or (webaddr == '')):
            return HttpResponseRedirect('learn')

        try:
            awebname = models.Learningweb.objects.get(webname=webname,user_id=auser.id)
            print('Duplicate web name.')
            return HttpResponseRedirect('learn')
        except Exception as e:
            pass
        try:
            aweb = models.Learningweb.objects.create(webname=webname, webaddr=webaddr, user=auser)
            webs = auser.learningweb_set.all()
            return render(request, "learn_eng_website_list.html", locals())
        except Exception as e:
            print(e)
            return render(request, "learn_eng_website_list.html")


@check_login
def del_review(request, word):
    print('del')
    # print(word)
    uid = request.session['user']['id']
    # print(uid)
    aword = models.Vocab.objects.get(vocab=word, user_id=uid)
    aword.delete()
    aud_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/audio/'
    img_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/images/'
    # root_path = os.getcwd()
    # audio_file = root_path+'/static/audio/'+ str(aword.audio)
    #
    # os.remove(audio_file)
    # os.chdir('/home/ubuntu/TeduProject/learnsite/learnword/static/images/')
    # os.system('rm -rf %s*.*' %aword.vocab)
    # print(type(aword.image))
    # print(aword.image)
    return HttpResponseRedirect('/t1/vocab/review')

@check_login
def sorting(request):
    id = request.session['user']['id']
    all_words = models.Vocab.objects.filter(user_id = id)
    counter = request.GET.get('counter')
    during = request.GET.get('during')
    if counter == "":
        counter = 999999
    else:
        counter = int(counter)
    if during == "":
        during = 999999
    else:
        during = int(during)
    print(counter, during)
    dtn = datetime.datetime.now(datetime.timezone.utc)
    words = []
    for word in all_words:
        time_delta = int((dtn-word.created_time).days)+1
        if int(word.review_cycle) <= counter and time_delta <= during:
            print(word.vocab)
            word.delta = time_delta
            words.append(word)


    print(words)
    return render(request, 'review_list.html', locals())
    # return HttpResponseRedirect('review')

@check_login
def del_website(request):
    print('del_website')
    id = request.session['user']['id']
    webname = request.POST.get('webname','')
    webaddr = request.POST.get('webaddr','')
    webname = webname.strip('')
    try:
        awebname = models.Learningweb.objects.get(webname=webname,user_id=id)
        awebname.delete()
        data = {
            'result': 'del_ok',
            'rwebname': '',
            'rwebaddr': '',
        }
    except Exception as e:
        print(e)
        data = {
            'result': 'del_NG',
            'rwebname': '',
            'rwebaddr': '',
        }
    return HttpResponse(json.dumps(data), content_type='application/json')


@check_login
def mod_website(request):
    print('mod_website')
    id = request.session['user']['id']
    webname = request.POST.get('webname','').strip('')
    webaddr = request.POST.get('webaddr','').strip('')

    try:
        aweb = models.Learningweb.objects.get(webname=webname, user_id=id)
        aweb.webname = webname
        aweb.webaddr = webaddr
        aweb.save()
        data = {
            'result': 'mod_ok',
            'rwebname': '',
            'rwebaddr': '',
        }

    except Exception as e:
        print(e)
        data = {
            'result': 'mod_error',
            'rwebname': 'Not exist for 學習網站',
            'rwebaddr': webaddr,
        }
    return HttpResponse(json.dumps(data), content_type='application/json')

