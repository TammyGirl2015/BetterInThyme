from django.urls import path
from bookings import views as booking_views  # Ensure this line is present

urlpatterns = [
    path('', booking_views.book_table, name='home'), 
]
