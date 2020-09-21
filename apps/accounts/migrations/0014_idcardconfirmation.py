# Generated by Django 2.2.10 on 2020-09-08 14:32

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200609_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='IDCardConfirmation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=30)),
                ('confirmation_uuid', models.CharField(blank=True, default=uuid.uuid4, max_length=255)),
                ('mobile_phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', help_text='United States phone numbers only.', max_length=128)),
                ('mobile_phone_number_verified', models.BooleanField(blank=True, default=False)),
                ('email', models.CharField(blank=True, default='', max_length=254)),
                ('email_verified', models.BooleanField(blank=True, default=False)),
                ('details', models.TextField(blank=True, default='')),
            ],
        ),
    ]
