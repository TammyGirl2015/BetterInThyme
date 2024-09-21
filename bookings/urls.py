from django.urls import path
from .views import booking_table

urlpatterns = [
    path('', booking_table, name='booking_table'), 
]
