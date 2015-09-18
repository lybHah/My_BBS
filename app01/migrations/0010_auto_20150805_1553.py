# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_bbs_total_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs_user',
            name='phone_num',
            field=models.IntegerField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bbs_user',
            name='sex',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bbs_user',
            name='sexual_orientation',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs_user',
            name='photo',
            field=models.ImageField(default=b'/static/images/shit.png', upload_to=b'/project/bbs_pro/statics/upload_imgs/'),
        ),
    ]
