from django.conf.urls import url
from . import views
from .views import (
    RoomList,
    RoomDetail,
   # CourseCreation,
   # CourseUpdate,
   # CourseDelete
)


urlpatterns = [
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^rooms$', RoomList.as_view(), name='rooms_list'),
    url(r'^rooms/new$', views.create_room, name='new_room'),
    url(r'^room/(?P<pk>\d+)$', RoomDetail.as_view(), name='room_detail'),
    url(r'^profile$', RoomDetail.as_view(), name='room_detail'),
]
