# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('WebSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='projection',
            name='type',
            field=models.SmallIntegerField(choices=[(1, '2D'), (2, '3D'), (3, '4D'), (4, '4DX')], validators=[django.core.validators.MinValueValidator(0)], default=1),
        ),
    ]
