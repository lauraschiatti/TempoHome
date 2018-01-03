from django.conf.urls import url, patterns
from . import views
from .views import (
    RoomList,
    RoomDetail,
    # RoomUpdate
    RoomDelete
)

urlpatterns = [
    url(r'^account/dashboard$', views.dashboard, name="dashboard"),
    url(r'^account/rooms$', RoomList.as_view(), name='rooms_list'),
    url(r'^account/rooms/new$', views.create_room, name='new_room'),
    url(r'^account/room/(?P<pk>\d+)$', RoomDetail.as_view(), name='room_detail'),
    url(r'^account/room/delete/(?P<pk>\d+)$', RoomDelete.as_view(), name='room_delete'),
    url(r'^search', views.search, name="search"),
]