# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 10:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_auto_20171205_1300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ('-postdate',)},
        ),
    ]
