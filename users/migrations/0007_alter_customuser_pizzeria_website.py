# Generated by Django 3.2.3 on 2021-08-01 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_pizzeria_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pizzeria_website',
            field=models.URLField(blank=True, verbose_name='Main Pizzeria Website'),
        ),
    ]
