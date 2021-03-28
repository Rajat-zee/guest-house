from django.urls import path
from .views import RoomApiView,BookingApiView

urlpatterns = [
       path('room/', RoomApiView.as_view() , name='RoomApiView'),
       path('booking/', BookingApiView.as_view() , name='BookingApiView'),
              ]