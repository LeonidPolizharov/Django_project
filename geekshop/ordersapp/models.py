from importlib.metadata import PathDistribution
from django.contrib.auth import get_user_model
from django.db import models
from mainapp.models import Product


class Order(models.Model):
    CREATED = 'CREATED'
    PAID = 'PAID'
    SENT = 'SENT'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = [
        (CREATED, 'Создан'),
        (PAID , 'Оплачен'),
        (SENT , 'Отправлен'),
        (DELIVERED , 'Доставлен'),
        (CANCELLED , 'Отменён'),
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='orders'
    )
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=CREATED)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def can_pay(self):
        return self.status == Order.CREATED

    @property
    def can_cancel(self):
        return self.status in (Order.CREATED, Order.PAID)


class OrderItemManager(models.Manager):
    def quantity(self):
        return sum(item.quantity for item in self.all())

    def sum(self):
        return sum(item.product.price * item.quantity for item in self.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    objects = OrderItemManager()


    @property
    def cost(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product} - {self.quantity} шт.'