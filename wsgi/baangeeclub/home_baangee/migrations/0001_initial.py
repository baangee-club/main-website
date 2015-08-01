# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=400)),
                ('image1', models.ImageField(upload_to=b'programme', blank=True)),
                ('image2', models.ImageField(upload_to=b'programme', blank=True)),
                ('image3', models.ImageField(upload_to=b'programme', blank=True)),
            ],
        ),
    ]
