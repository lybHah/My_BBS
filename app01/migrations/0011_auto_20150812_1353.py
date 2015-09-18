# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20150805_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bbs',
            options={'ordering': ['-created_at'], 'verbose_name': '\u5e16\u5b50', 'verbose_name_plural': '\u5e16\u5b50'},
        ),
        migrations.AlterModelOptions(
            name='bbs_user',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u677f\u5757', 'verbose_name_plural': '\u677f\u5757'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AddField(
            model_name='bbs',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='phone_num',
            field=models.IntegerField(default=10086),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='sex',
            field=models.IntegerField(default=3, choices=[(0, '\u7537'), (1, '\u5973'), (2, '\u5176\u4ed6')]),
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='sexual_orientation',
            field=models.IntegerField(default=1, choices=[(0, '\u540c\u6027\u604b'), (1, '\u5f02\u6027\u604b'), (2, '\u53cc\u6027\u604b'), (3, '\u8de8\u79cd\u65cf')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
