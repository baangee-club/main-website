# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exp_title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('board', models.CharField(max_length=100)),
                ('marks', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField(verbose_name=b'Date Of Birth')),
                ('token', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('mobile_no', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('dob', models.DateField(verbose_name=b'Date Of Birth')),
                ('token', models.ForeignKey(blank=True, to='career_786ms.Token', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='qualification',
            name='user',
            field=models.ForeignKey(to='career_786ms.User'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(to='career_786ms.User'),
        ),
    ]
