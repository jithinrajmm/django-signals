from django.db.models.signals import pre_save

from django.dispatch import receiver
from cars.models import Car
from buyers.models import Buyer
import uuid

@receiver(pre_save,sender = Car)
def pre_save_create_code(sender,instance,**kwargs):
    if instance.car_number == "":
        instance.car_number = str(uuid.uuid4()).upper().replace('-','')[0:5]

    obj = Buyer.objects.get(user = instance.buyer.user)
    obj.from_signals = True
    obj.save()