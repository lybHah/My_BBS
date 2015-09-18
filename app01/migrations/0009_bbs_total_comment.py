# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_bbs_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='total_comment',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
