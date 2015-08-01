# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0006_auto_20150801_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='desciption',
            new_name='description',
        ),
    ]
