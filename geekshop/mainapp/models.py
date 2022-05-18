from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=140)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_image/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}: {self.name}'
