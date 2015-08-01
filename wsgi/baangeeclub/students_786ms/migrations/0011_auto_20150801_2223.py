# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_786ms', '0010_auto_20150801_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttoken',
            name='token',
            field=models.CharField(default=b' ', unique=True, max_length=8, editable=False),
        ),
    ]
