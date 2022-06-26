from email.policy import default
from unicodedata import category
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=140)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_image/', default='default.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


@receiver(pre_save, sender=Category)
def update_product_is_active(sender, instance, **kwargs):
    old_category = Category.objects.filter(pk=instance.pk).first()
    if old_category and old_category.is_active != instance.is_active:
        Product.objects.filter(category=instance).update(is_active=instance.is_active)