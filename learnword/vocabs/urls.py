#file: vocabs/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^review_word/(?P<word>\w+)$',views.reviewword),
    url(r'^review/sorting$',views.sorting),
    url(r'^review/del/(?P<word>\w+)',views.del_review),
    url(r'^review',views.review),
    url(r'^learn/del_website$',views.del_website),
    url(r'^learn/mod_website$',views.mod_website),
    url(r'^learn',views.learn_eng_website_list),


]

