# Generated by Django 5.1.4 on 2024-12-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0009_alter_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
