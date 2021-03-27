from django.urls import path
from .views import RoomListView, BookingListView, RoomDetailView, CancelBookingView,HomeView,AboutView,ContactView

app_name='ca'

urlpatterns = [
       #NAV
       path('home/', HomeView, name='HomeView'),
       path('home/about', AboutView, name='AboutView'),
       path('home/contact', ContactView, name='ContactView'),
       #Rooms
       path('home/room_list/', RoomListView, name='RoomListView'),
       path('home/room_list/room/<r_no>', RoomDetailView.as_view(), name='RoomDetailView'),
       #bookings
       path('booking_list/', BookingListView.as_view(), name='BookingListView'),    
       path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),

              ]