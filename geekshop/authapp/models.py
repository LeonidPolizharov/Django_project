from distutils.command.upload import upload
import uuid
from datetime import timedelta
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_activation_key_expires():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    city = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to="user_images", blank=True)

    activation_key = models.UUIDField(default=uuid.uuid4)
    activation_key_expires = models.DateTimeField(default=get_activation_key_expires)

    @property
    def is_activation_key_expires(self):
        return now() > self.activation_key_expires

    def activate(self):
        self.is_active = True
        self.activation_key_expires = now()
    