from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import BookingForm

def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Add redirect or success message here
    else:
        form = BookingForm()
    return render(request, 'bookings/book_table.html', {'form': form})
