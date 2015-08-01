# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0004_auto_20150801_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='album',
            field=models.ForeignKey(blank=True, to='home_baangee.Album', null=True),
        ),
    ]
