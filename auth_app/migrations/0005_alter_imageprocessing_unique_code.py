# Generated by Django 5.1.4 on 2024-12-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_alter_imageprocessing_unique_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageprocessing',
            name='unique_code',
            field=models.CharField(max_length=20),
        ),
    ]