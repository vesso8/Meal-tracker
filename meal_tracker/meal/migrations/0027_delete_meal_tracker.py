# Generated by Django 4.0.3 on 2022-09-24 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0026_rename_products_meal_tracker_meal_tracker_products'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meal_tracker',
        ),
    ]
