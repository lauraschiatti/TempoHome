from django.conf.urls import url
from . import views
from .views import (
    RoomList,
    RoomDetail,
    RoomDelete,
    RequestList,
    RequestUpdate
)

urlpatterns = [
    url(r'^account/dashboard$', views.dashboard, name="dashboard"),
    url(r'^account/rooms$', RoomList.as_view(), name='rooms_list'),
    url(r'^account/rooms/new$', views.create_room, name='new_room'),
    url(r'^account/room/(?P<pk>\d+)$', RoomDetail.as_view(), name='room_detail'),
    url(r'^account/room/delete/(?P<pk>\d+)$', RoomDelete.as_view(), name='room_delete'),
    url(r'^search', views.search, name="search"),
    url(r'^send-request', views.post_request, name="post_request"),
    url(r'^account/requests$', RequestList.as_view(), name='requests_list'),
    url(r'^account/requests/(?P<pk>\d+)/edit$', RequestUpdate.as_view(), name='request_edit'),
    url(r'^account/responses$', views.responses_list, name='responses_list'),
]