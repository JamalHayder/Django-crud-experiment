# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-06-02 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20190601_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trivia',
            old_name='trivia',
            new_name='trivia_details',
        ),
    ]
