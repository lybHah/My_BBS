# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_remove_bbs_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='category',
            field=models.ForeignKey(default=1, to='app01.Category'),
            preserve_default=False,
        ),
    ]
