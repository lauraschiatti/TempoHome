from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup', views.sign_up, name="sign_up"),
]