#file: vocabs/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^review_word',views.reviewword),
    url(r'^review',views.review),

    url(r'^learn',views.learn_eng_website_list),
]


