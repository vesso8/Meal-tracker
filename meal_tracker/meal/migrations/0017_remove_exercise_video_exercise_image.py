# Generated by Django 4.0.3 on 2022-05-30 20:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0016_remove_exercise_image_exercise_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='video',
        ),
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
