# Generated by Django 4.0.3 on 2022-10-30 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0035_calorie_counter_quantity_is_less'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='quantity_units',
            field=models.CharField(choices=[('(gr)', '(gr)'), ('(kg)', '(kg)'), ('(l)', '(l)'), ('(ml)', '(ml)'), ('(per piece)', '(per piece)')], max_length=11),
        ),
    ]
