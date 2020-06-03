# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_baangee', '0007_auto_20150801_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('creation_time', models.DateTimeField(default=datetime.datetime.now)),
                ('image1', models.ImageField(null=True, upload_to=b'article', blank=True)),
                ('image2', models.ImageField(null=True, upload_to=b'article', blank=True)),
                ('image3', models.ImageField(null=True, upload_to=b'article', blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
