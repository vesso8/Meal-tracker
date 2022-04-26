# Generated by Django 4.0.3 on 2022-04-04 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
