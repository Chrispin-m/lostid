# Generated by Django 5.1.3 on 2024-12-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundid',
            name='thumbnail',
            field=models.ImageField(blank=True, editable=False, null=True, upload_to='found_ids/thumbnails/'),
        ),
    ]
