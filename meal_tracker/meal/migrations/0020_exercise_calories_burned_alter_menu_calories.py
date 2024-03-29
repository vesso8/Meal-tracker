# Generated by Django 4.0.3 on 2022-05-30 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0019_alter_exercise_muscle_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='calories_burned',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='calories',
            field=models.PositiveIntegerField(),
        ),
    ]
