# file: users/urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login', views.login),
    url(r'^reg', views.registor),
    url(r'^logout', views.logout),
    url(r'^infor', views.infor),

]

