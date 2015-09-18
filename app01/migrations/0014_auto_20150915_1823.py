# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0013_auto_20150915_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='sex',
            field=models.IntegerField(default=2, choices=[(0, '\u7537'), (1, '\u5973'), (2, '\u5176\u4ed6')]),
        ),
    ]
