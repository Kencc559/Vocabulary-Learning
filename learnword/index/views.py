#file: index/views.py
import glob
import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
# from spider.Yahoo import Yahoo
import redis
import json
from scrapyd_api import ScrapydAPI
# from django.core.cache import cache
from vocabs import models

scrapyd = ScrapydAPI('http://localhost:6800')
redis_db = redis.Redis(host='127.0.0.1', port=6379, db=0)
def index(request):

    if request.method == "GET":
        search = ''
        if (not hasattr(request, 'session')) or ('user' not in request.session):
            return render(request, "index.html")
        index = {
            'login': 'ok',
            'infor': request.session['user']['username'],
        }
        # cache.set('v', '555', 60*60)
        # print(cache.has_key('v'))
        # print(cache.get('v'))
        return render(request, "index.html", locals())

    elif request.method == "POST":
        search = 'ok'
        searchword = request.POST.get('searchWord','0')
        print(searchword)
        if not redis_db.exists(searchword):
            os.chdir('/home/ubuntu/TeduProject/spider/Yahoo')
            os.system('scrapy crawl yahoo -a inquireWord=%s' %searchword)

        try:
            sword = redis_db.keys(searchword)[0].decode()
        except:
            search = 'NG'
            return render(request, "index.html", locals())
        # printOut(searchword, 'chinese')
        # print(sword[0].decode())
        chinese = redis_db.hget(searchword, 'chinese').decode('unicode_escape')

        chinese_dic = json.loads(chinese)
        # word_type = []
        # trans = []
        # for k, v in chinese_dic.items():
        # # print(k, v)
        #     print(k,"*"*50)
        #     print(v,"*"*50)
        #     word_type.append(k)
        #     trans.append(v)
        # print(word_type)
        # print(trans)
        # chinese_dic ={
        #     'word_type':word_type,
        #     'trans':trans
        # }


        audio = redis_db.hget(searchword, 'audio').decode()
        # printOut(searchword, 'images')
        images = redis_db.hget(searchword, 'images').decode('unicode_escape')
        images = json.loads(images)
        imgs1 = []
        imgs2 = []
        i = 0
        for name in images:
            if i < 2:
                imgs1.append(name)
            else:
                imgs2.append(name)
            i += 1
        # print(imgs1,imgs2,"*"*50)
        # task = scrapyd.schedule('Yahoo', 'yahoo',searchword=searchword)
        # print('Task: ',task)
        # print(chinese_dic,"*"*50)
        if (not hasattr(request, 'session')) or ('user' not in request.session):
            return render(request,"index.html", locals())
        index = {
            'login': 'ok',
            'infor': request.session['user']['username'],
        }

        return render(request,"index.html", locals())
        # return HttpResponse('searchword: '+ chinese +'<br>'+audio+',<br>'+images)

# def printOut(qword, pout):
#     out_json = redis_db.hget(qword, pout)
#     out_dic = json.loads(out_json)
#     for k, v in out_dic.items():
#         print(k, v)

def save_word(request):

    sword = request.POST.get('word','')
    uid = request.session['user']['id']

    try:
        aword = models.Vocab.objects.get(vocab=sword,user_id=uid)
        mesg = 'Save duplicated !!'
        audio_file = ''
        imgs_file =''
        chinese_dic = ''
    except:
        audio_path = request.POST.get('audio_path', '')
        imgs_path = request.POST.get('imgs_path', '')
        chinese = redis_db.hget(sword, 'chinese').decode('unicode_escape')
        chinese_dic = json.loads(chinese)
        chinese_json = json.dumps(chinese_dic, ensure_ascii=False)
        # print(chinese_json)
        # print(type(chinese_json))
        print('*'*20)
        audio_file = cp_file('audio', sword)
        imgs_file = cp_file('img', sword)
        aword = models.Vocab.objects.create(vocab=sword,
                                            chinese=chinese_json,
                                            audio=audio_file,
                                            image=imgs_file,
                                            user_id=uid)
        mesg = 'Save ok'
    print(audio_file)
    data = {
        'word': sword,
        'audio_path' : audio_file,
        'imgs_path' : imgs_file,
        'chinese' : chinese_json,
        'mesg' : mesg,
    }
    return HttpResponse(json.dumps(data), content_type= 'application/json')

def cp_file(media, word):
    if media == 'audio':
        r_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/audio/load/'
        w_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/audio/'
        r_file = glob.glob(os.path.join(r_dir, '*.mp3'))[0]
        audio_file = r_file.split('/')[-1]
        # r_file = r_dir + '%s.mp3' %word
        with open(r_file, 'rb') as f:
            audio = f.read()

        w_file = os.path.join(w_dir, audio_file)
        with open(w_file, 'wb') as f:
            f.write(audio)

        return str(audio_file)

    elif media == 'img':
        r_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/images/load/'
        w_dir = '/home/ubuntu/TeduProject/learnsite/learnword/static/images/'
        imgs = []
        img_path_files = glob.glob(os.path.join(r_dir, '*'))
        for img in img_path_files:
            img_file = img.split('/')[-1]
            r_file = os.path.join(r_dir,img_file)
            with open(r_file, 'rb') as f:
                img = f.read()
            w_file = os.path.join(w_dir,img_file)
            with open(w_file, 'wb') as f:
                f.write(img)
            imgs.append(img_file)
            imgs_str = ",".join(imgs)
        return imgs_str
    else:
        return False




    #
    # if not os.path.exists(w_dir):
    #     os.makedirs(w_dir)
    # file = w_dir + '{}.mp3'.format(word)