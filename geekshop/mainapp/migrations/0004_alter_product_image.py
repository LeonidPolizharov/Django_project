# Generated by Django 3.2.11 on 2022-04-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_image/'),
        ),
    ]
