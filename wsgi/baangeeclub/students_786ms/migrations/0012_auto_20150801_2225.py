# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import students_786ms.models


class Migration(migrations.Migration):

    dependencies = [
        ('students_786ms', '0011_auto_20150801_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttoken',
            name='token',
            field=models.CharField(default=students_786ms.models.get_token, unique=True, max_length=8, editable=False),
        ),
    ]
