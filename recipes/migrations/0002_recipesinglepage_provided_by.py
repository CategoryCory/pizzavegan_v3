# Generated by Django 3.1.2 on 2020-11-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipesinglepage',
            name='provided_by',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
