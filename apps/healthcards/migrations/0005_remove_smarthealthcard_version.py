# Generated by Django 2.2.18 on 2021-04-28 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthcards', '0004_auto_20210423_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smarthealthcard',
            name='version',
        ),
    ]
