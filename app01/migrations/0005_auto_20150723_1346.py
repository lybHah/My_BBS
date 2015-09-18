# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20150723_1337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(default=1, to='app01.BBS_user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='bbs_id',
            field=models.IntegerField(),
        ),
    ]
