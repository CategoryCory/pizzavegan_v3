# Generated by Django 3.2.3 on 2021-06-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20210621_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzerialocation',
            name='carry_out',
            field=models.BooleanField(default=False, verbose_name='Carry Out'),
        ),
        migrations.AddField(
            model_name='pizzerialocation',
            name='delivery',
            field=models.BooleanField(default=False, verbose_name='Delivery'),
        ),
        migrations.AddField(
            model_name='pizzerialocation',
            name='dine_in',
            field=models.BooleanField(default=False, verbose_name='Dine In'),
        ),
        migrations.AddField(
            model_name='pizzerialocation',
            name='phone',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
