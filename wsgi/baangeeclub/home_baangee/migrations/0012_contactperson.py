# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0011_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('mobile_number', models.CharField(max_length=100)),
            ],
        ),
    ]
