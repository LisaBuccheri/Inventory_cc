# Generated by Django 5.0.6 on 2024-05-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0002_ingredient_name_ingredient_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
