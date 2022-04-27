from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

class ShopUser(AbstractUser):
    city = models.CharField(max_length=64, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)

    