# Generated by Django 2.2.18 on 2021-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20210505_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='public_safety_profile',
            field=models.CharField(blank=True, choices=[('PUBLIC', 'Public'), ('PRIVATE', 'Private')], default='PRIVATE', max_length=16),
        ),
    ]
