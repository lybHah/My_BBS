# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20150719_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
