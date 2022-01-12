#file: index/urls.py

from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$',views.index),
    url(r'^index/save/$', views.save_word),
]