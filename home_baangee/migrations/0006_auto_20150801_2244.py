# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0005_auto_20150801_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='creation_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='photo',
            name='uploading_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='programme',
            name='image1',
            field=models.ImageField(null=True, upload_to=b'programme', blank=True),
        ),
        migrations.AlterField(
            model_name='programme',
            name='image2',
            field=models.ImageField(null=True, upload_to=b'programme', blank=True),
        ),
        migrations.AlterField(
            model_name='programme',
            name='image3',
            field=models.ImageField(null=True, upload_to=b'programme', blank=True),
        ),
    ]
