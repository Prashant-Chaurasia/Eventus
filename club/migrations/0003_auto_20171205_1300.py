# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 07:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20171205_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='logo',
            new_name='club_image',
        ),
    ]
