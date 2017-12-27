from django.conf.urls import url
from . import views
from .views import (
    RoomList
   # CourseDetail,
   # CourseCreation,
   # CourseUpdate,
   # CourseDelete
)


urlpatterns = [
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^rooms$', RoomList.as_view(), name='rooms_list'),
    url(r'^rooms/new$', views.create_room, name='new_room'),

]
