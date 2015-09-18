# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20150725_1125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='category',
        ),
    ]
