# Generated by Django 3.2.11 on 2022-05-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_shopuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
