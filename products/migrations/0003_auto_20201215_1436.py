# Generated by Django 3.1.2 on 2020-12-15 20:36

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productsinglepage_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='productsinglepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='products.ProductCategory'),
        ),
    ]