# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0008_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='uploading_time',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='programme',
            name='description',
            field=models.TextField(),
        ),
    ]
