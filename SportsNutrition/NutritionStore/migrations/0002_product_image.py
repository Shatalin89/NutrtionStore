# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-28 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NutritionStore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='/media/')),
                ('image_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NutritionStore.products')),
            ],
        ),
    ]
