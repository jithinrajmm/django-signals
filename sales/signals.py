from django.db.models.signals import post_delete

from django.dispatch import receiver

from orders.models import Order

from sales.models import Sale

@receiver(post_delete,sender = Sale)
def post_delete_change_active_order(sender,instance,**kwargs):
    obj = instance.order
    obj.active = False
    obj.save()