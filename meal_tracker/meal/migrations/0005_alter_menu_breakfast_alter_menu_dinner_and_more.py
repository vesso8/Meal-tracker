# Generated by Django 4.0.3 on 2022-04-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_remove_menu_ingredients_menu_breakfast_menu_dinner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='breakfast',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dinner',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='lunch',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='menu',
            name='snack_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='snack_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='snack_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
