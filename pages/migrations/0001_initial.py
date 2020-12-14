# Generated by Django 3.1.2 on 2020-12-14 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('click', 'Click'), ('hover', 'Hover'), ('view', 'View')], default='click', max_length=25)),
                ('event_time', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.CharField(default='0.0.0.0', max_length=20)),
                ('zip_code', models.CharField(default='', max_length=15)),
            ],
            options={
                'verbose_name': 'Ad Data',
                'verbose_name_plural': 'Ad Data',
            },
        ),
    ]
