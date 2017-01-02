# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0003_auto_20150801_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('desciption', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'gallery')),
                ('album', models.ForeignKey(to='home_baangee.Album')),
            ],
        ),
        migrations.AddField(
            model_name='programme',
            name='album',
            field=models.ForeignKey(default=1, blank=True, to='home_baangee.Album'),
            preserve_default=False,
        ),
    ]
