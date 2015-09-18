# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0012_auto_20150915_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='phone_num',
            field=models.IntegerField(default=10086, null=True, blank=True),
        ),
    ]
