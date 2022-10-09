# Generated by Django 4.0.3 on 2022-05-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0017_remove_exercise_video_exercise_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='fifth_exercise',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='first_exercise',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='fourth_exercise',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='second_exercise',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exercise',
            name='sixth_exercise',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='third_exercise',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
