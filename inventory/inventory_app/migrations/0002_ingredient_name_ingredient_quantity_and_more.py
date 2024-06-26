# Generated by Django 5.0.6 on 2024-05-24 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='unit_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default='plat', max_length=100),
        ),
        migrations.AddField(
            model_name='purchases',
            name='menu_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_app.menuitem'),
        ),
        migrations.AddField(
            model_name='purchases',
            name='time_stamp',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='ingredient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_app.ingredient'),
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='menu_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_app.menuitem'),
        ),
        migrations.AddField(
            model_name='reciperequirement',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
