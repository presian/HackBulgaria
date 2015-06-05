# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebSystem', '0002_auto_20150521_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projection',
            name='time',
        ),
        migrations.AlterField(
            model_name='projection',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
