# Generated by Django 3.0.8 on 2020-08-20 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Submission', '0004_auto_20200820_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='NumberOfRooms',
        ),
    ]