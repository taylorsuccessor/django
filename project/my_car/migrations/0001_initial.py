# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-11 20:24
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import my_car.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=5)),
                ('price', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('number_of_door', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of Doors')),
                ('temperature', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('AE', 'available'), ('AE', 'not available')], max_length=2, null=True)),
                ('show', models.NullBooleanField(default=False)),
                ('img', models.FileField(upload_to=my_car.models.get_upload_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('edited_at', models.DateTimeField(blank=True, null=True, verbose_name='Edited At')),
                ('deleted_at', models.DateField(blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='mycar',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='my_car.Shop'),
        ),
    ]
