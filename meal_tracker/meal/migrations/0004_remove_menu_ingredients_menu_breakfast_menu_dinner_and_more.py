# Generated by Django 4.0.3 on 2022-04-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='menu',
            name='breakfast',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='dinner',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='lunch',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='snack_1',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='snack_2',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='snack_3',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
