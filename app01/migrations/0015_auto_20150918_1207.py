# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20150915_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbs',
            name='ranking',
        ),
        migrations.AlterField(
            model_name='bbs',
            name='total_comment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bbs',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
