
from django.shortcuts import render
from .forms import BookingForm

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()
    
    return render(request, 'bookings/book_table.html', {'form': form})
