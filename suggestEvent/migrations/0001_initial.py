# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 07:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_auto_20171204_1116'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Details', models.CharField(max_length=500)),
                ('upvotes', models.IntegerField(blank=True)),
                ('downvotes', models.IntegerField(blank=True)),
                ('postdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('Code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.CollegeCode')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
