# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_auto_20150812_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs_user',
            name='phone_num',
            field=models.IntegerField(default=10086, blank=True),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='signature',
            field=models.CharField(default=b'This gay is too lazy to leave anything here.', max_length=50),
        ),
    ]
