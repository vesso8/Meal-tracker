# Generated by Django 4.0.3 on 2022-11-22 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0040_remove_exercise_fifth_exercise_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercise',
            field=models.TextField(max_length=255),
        ),
    ]