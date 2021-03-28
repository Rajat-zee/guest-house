from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .serializers import RoomSerializer, BookingSerializer
from ca.models import Room, Booking

# Create your views here.

class RoomApiView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
    def get(self,request):
        return self.list(request)

class BookingApiView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    def get(self,request):
        return self.list(request)
    

    
    
