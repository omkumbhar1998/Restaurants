# Generated by Django 3.0.4 on 2020-04-20 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200419_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account',
        ),
    ]
