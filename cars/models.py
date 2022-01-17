from django.db import models
from buyers.models import Buyer

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length = 200)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer,on_delete = models.CASCADE)
    car_number = models.CharField(max_length = 100,blank=True)

    def __str__(self):
        return f"{self.name}+ {self.price} + {self.buyer}"
