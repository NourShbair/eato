# Generated by Django 4.2.19 on 2025-04-04 18:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eato_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="image",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="image"
            ),
        ),
    ]
