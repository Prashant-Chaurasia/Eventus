# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20171119_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='city',
        ),
    ]