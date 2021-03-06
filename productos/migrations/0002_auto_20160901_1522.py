# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcat',
        ),
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat', to='productos.Subcat'),
        ),
        migrations.AddField(
            model_name='subcat',
            name='caty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='productos.Category'),
        ),
    ]
