from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView , FormView , View, DeleteView
from django.urls import reverse , reverse_lazy
from .models import Room , Booking
from .forms import AvailabilityForm
from ca.booking_functions.availability import check_availability

# Create your views here.

def HomeView(request):
    template_name='index.html'
    return render(request,'index.html')
def AboutView(request):
    template_name='about.html'
    return render(request,'about.html')
def ContactView(request):
    template_name='contact.html'
    return render(request,'contact.html')



#ROOOOMMMMSSSS
def RoomListView(request):
    room = Room.objects.all()[0]
    room_r_no = dict(room.r_no_cho)
    room_values = room_r_no.values()

    room_list =[]
    
    for rno in room_r_no:
        room = room_r_no.get(rno)
        room_url = reverse('ca:RoomDetailView', kwargs={
                           'r_no':rno})
        room_list.append((room,room_url))
    
    context={
        'room_list':room_list,
    }
    return render(request, 'room_list_view.html', context) 



class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        r_no = self.kwargs.get('r_no', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(r_no=r_no)

        if len(room_list) > 0:
            room = room_list[0]
            room_r_no = dict(room.r_no_cho).get(room.r_no,None)
            context = {
                'room_r_no': room_r_no,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('r_no doesnot exist')
        

    def post(self, request, *args, **kwargs):
        r_no = self.kwargs.get('r_no', None)
        room_list = Room.objects.filter(r_no=r_no)
        form = AvailabilityForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)

        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out']
            )
            booking.save()
            messages.info(request, 'Your booking is succesful')
            return HttpResponseRedirect('/booking_list/')
        else:
            messages.info(request, 'All of this category of rooms are booked!! Try another one')
            return HttpResponseRedirect('/home/room_list/')


#BOOOKKIINNGGSSS
class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list_view.html'

    def get_queryset(self,*args,**kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list

class CancelBookingView(DeleteView):
    model = Booking
    template_name = 'booking_cancel_view.html'
    success_url = reverse_lazy('ca:BookingListView')
