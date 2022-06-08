# Generated by Django 3.2.11 on 2022-06-06 18:25

import authapp.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_shopuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=authapp.models.get_activation_key_expires),
        ),
    ]