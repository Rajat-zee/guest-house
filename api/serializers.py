from rest_framework import serializers as s
from ca.models import Room, Booking

class RoomSerializer(s.ModelSerializer):
    
    class Meta:
        model = Room
        fields = ['id','r_no','ppl']

class BookingSerializer(s.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ['id','room','name','emp_no','check_in','check_out']