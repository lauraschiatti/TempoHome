from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^signup/$', views.sign_up, name="signup"),
    url(r'^login/$', views.authentication, name="login"),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^account/profile/(?P<username>\w+)$', views.get_profile, name="get_profile")
]