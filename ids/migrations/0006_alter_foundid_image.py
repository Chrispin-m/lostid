# Generated by Django 5.1.3 on 2024-12-04 14:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ids', '0005_remove_foundid_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundid',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]