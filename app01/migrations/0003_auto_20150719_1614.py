# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='bbs_id',
            field=models.ForeignKey(to='app01.BBS'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(to='app01.BBS_user'),
        ),
    ]
