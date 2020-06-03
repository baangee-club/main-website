# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0002_guest_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(unique=True, max_length=254),
        ),
    ]
