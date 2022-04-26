# Generated by Django 4.0.3 on 2022-04-13 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meal', '0011_alter_food_person_of_alter_meal_tracker_person_of'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='person_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='meal_tracker',
            name='person_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
