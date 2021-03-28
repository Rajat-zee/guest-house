from django.urls import path
from .views import RoomListView, RoomListView1, BookingListView, RoomDetailView, CancelBookingView, HomeView, HomeView1, AboutView, ContactView

app_name='ca'

urlpatterns = [
       #NAV
       path('home/', HomeView, name='HomeView'),
       path('home1/', HomeView1, name='HomeView1'),
       path('home/about', AboutView, name='AboutView'),
       path('home/contact', ContactView, name='ContactView'),
       path('home1/about', AboutView, name='AboutView'),
       path('home1/contact', ContactView, name='ContactView'),
       #Rooms
       path('home/room_list/', RoomListView1, name='RoomListView1'),
       path('home1/room_list/', RoomListView, name='RoomListView'),
       path('home1/room_list/room/<r_no>', RoomDetailView.as_view(), name='RoomDetailView'),
       #bookings
       path('booking_list/', BookingListView.as_view(), name='BookingListView'),    
       path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView'),

              ]