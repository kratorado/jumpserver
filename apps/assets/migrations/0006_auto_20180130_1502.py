# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-30 07:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0005_auto_20180126_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='cabinet_no',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='cabinet_pos',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='env',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='remote_card_ip',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='status',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='type',
        ),
    ]