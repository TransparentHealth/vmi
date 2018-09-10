# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-02 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20161025_0006'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InvitesAvailable',
        ),
        migrations.AlterModelOptions(
            name='invitation',
            options={'verbose_name': 'Developer Invite'},
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='requestinvite',
            name='user_type',
        ),
    ]