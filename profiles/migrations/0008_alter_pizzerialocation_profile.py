# Generated by Django 3.2.3 on 2021-06-21 01:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0007_menuitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzerialocation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to=settings.AUTH_USER_MODEL),
        ),
    ]
