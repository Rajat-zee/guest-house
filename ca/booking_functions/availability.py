import datetime
from ca.models import Room, Booking

def check_availability(room, check_in,check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    
    for i in booking_list:
        if i.check_in > check_out or i.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)