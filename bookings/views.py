
from django.shortcuts import render
from .forms import BookingForm 

def booking_table(request):
    form = BookingForm()  
    return render(request, 'bookings/booking_table.html', {'form': form})
