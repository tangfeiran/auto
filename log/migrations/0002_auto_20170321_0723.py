# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='task_id',
            new_name='task',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_id',
            new_name='ansible_task_id',
        ),
    ]
