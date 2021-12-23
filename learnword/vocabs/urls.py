#file: vocabs/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^review',views.review_view),
    url(r'^engwebsite',views.learn_eng_website_list_view),
]

