# Generated by Django 5.1.4 on 2024-12-18 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0011_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
