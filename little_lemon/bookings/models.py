from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.date} {self.time}"