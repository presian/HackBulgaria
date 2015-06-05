# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('WebSystem', '0004_auto_20150521_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='username',
            field=models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
