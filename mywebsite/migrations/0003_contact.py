# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(help_text='Name', max_length=200)),
                ('Email', models.CharField(help_text='Email', max_length=200)),
                ('Comment', models.TextField(help_text='Comment', max_length=1000)),
            ],
        ),
    ]
