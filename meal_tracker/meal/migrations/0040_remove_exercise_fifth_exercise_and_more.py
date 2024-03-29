# Generated by Django 4.0.3 on 2022-11-22 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0039_remove_calorie_counter_quantity_is_less_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='fifth_exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='first_exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='fourth_exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='second_exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='sixth_exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='third_exercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='exercise',
            field=models.TextField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
