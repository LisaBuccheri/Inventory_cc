# Generated by Django 5.0.6 on 2024-05-25 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0003_alter_menuitem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='menu_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='inventory_app.menuitem'),
        ),
    ]
