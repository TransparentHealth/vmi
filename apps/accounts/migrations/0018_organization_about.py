# Generated by Django 2.2.10 on 2020-09-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200929_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='about',
            field=models.TextField(blank=True, default=''),
        ),
    ]