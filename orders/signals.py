from django.db.models.signals import m2m_changed
from django.db.models.signals import post_save

from django.dispatch import receiver
from orders.models import Order
from sales.models import Sale

@receiver(m2m_changed,sender = Order.car.through)
def m2m_changed_orders(sender,instance,action,**kwargs):
    total = 0
    total_prize = 0
    print(action,'...........................................................')
    if action == 'post_add' or  action == 'post_remove':
        print(action)
        for car in instance.car.all():
            total += 1
            total_prize += car.price
        instance.total_car = total 
        instance.total_prize = total_prize
        instance.save()


@receiver(post_save,sender=Order)
def create_sale_amount_form_order_total_prize(sender,instance,created,**kwargs):
    obj,_ = Sale.objects.get_or_create(order= instance)
    obj.amout = instance.total_prize 
    obj.save()


