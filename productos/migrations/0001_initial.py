# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 15:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('subcat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('in_stock', models.BooleanField(default=True)),
                ('desc', models.TextField()),
                ('slug', models.SlugField(max_length=280)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='productos.Category')),
            ],
        ),
    ]
