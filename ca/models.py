from django.db import models as m
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Room(m.Model):

    r_no_cho=(
            (1,'Alpha'),
            (2,'Beta'),
            (3,'Gamma'),
            
             )
             
    r_no = m.IntegerField(max_length=None, choices=r_no_cho)
    ppl  = m.IntegerField(max_length=1)
   

    

    def __str__(self):
        return f'room no {self.r_no} '

class Booking(m.Model):
    user      = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE)
    room      = m.ForeignKey(Room , on_delete=m.CASCADE)
    name      = m.CharField(max_length=20)
    emp_no    = m.IntegerField(max_length=20, null=True)
    check_in  = m.DateTimeField()
    check_out = m.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked room no. {self.room} for {self.name} with empid:{self.emp_no} from {self.check_in} to {self.check_out}'
    
    def get_room_no(self):
        room_no = dict(self.room.r_no_cho)
        r_no = room_no.get(self.room.r_no)
        return r_no

    def get_cancel_booking_url(self):
        return reverse('ca:CancelBookingView',args=[self.pk,])

