# Generated by Django 3.1.11 on 2021-05-30 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='company_name',
        ),
    ]
