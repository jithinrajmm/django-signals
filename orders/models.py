from django.db import models
from cars.models import Car

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length = 100)
    car  = models.ManyToManyField(Car)
    total_car = models.PositiveIntegerField(blank=True,null=True)
    total_prize = models.PositiveIntegerField(blank = True, null = True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 
