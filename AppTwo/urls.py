from django.urls import re_path as url
from AppTwo import views

urlpatterns = [
    url(r'^$', views.store, name='store'),
    url(r'^help$', views.help, name='help'),
]