from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the Django User model
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Booking by {self.user.username} for Table {self.table.number} on {self.date} at {self.time}"
