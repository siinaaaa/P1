# Generated by Django 5.1.4 on 2024-12-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='color',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]