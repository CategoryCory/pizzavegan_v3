# Generated by Django 3.1.11 on 2021-05-30 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='company_name',
            field=models.CharField(default='', max_length=100, verbose_name='Company/Pizzeria Name'),
            preserve_default=False,
        ),
    ]
