from django.db import models

# Create your models here.
from django.db import models

class Table(models.Model):
    number = models.IntegerField()
    seats = models.IntegerField()

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    guests = models.IntegerField()
