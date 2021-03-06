# Generated by Django 2.2.18 on 2021-05-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0030_auto_20210428_1154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='subject_qrcode_public',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='public_safety_profile',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
