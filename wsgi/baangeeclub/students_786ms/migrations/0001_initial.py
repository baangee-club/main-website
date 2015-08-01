# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='StudentToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('token', models.CharField(default=b'B5390EE0', unique=True, max_length=8, editable=False)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('token', models.OneToOneField(related_name='student', primary_key=True, serialize=False, to='students_786ms.StudentToken')),
                ('care_of', models.CharField(default=(b'Parents', b'Parents'), max_length=100, choices=[(b'Parents', b'Parents'), (b'Gardians', b'Gardians')])),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('gender', models.CharField(default=(b'Male', b'Male'), max_length=100, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'others', b'others')])),
                ('date_of_birth', models.DateField()),
                ('category', models.CharField(default=(b'General', b'General'), max_length=100, choices=[(b'General', b'General'), (b'SC', b'SC'), (b'ST', b'ST'), (b'Other Backward Classes', b'Other Backward Classes')])),
                ('occupation', models.CharField(max_length=100, choices=[(b'Government', b'Government'), (b'Government undertaking', b'Government undertaking'), (b'self employed', b'self employed'), (b'others', b'others')])),
                ('mobile', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('distict', models.CharField(max_length=100)),
                ('pin_code', models.IntegerField()),
                ('highest_educational_qualification', models.CharField(max_length=100, choices=[(b'Others', b'Others'), (b'Graduation or higher', b'Graduation or higher'), (b'Polytechnic Diploma', b'Polytechnic Diploma'), (b'Below 10th', b'Below 10th'), (b'10th Pass', b'10th Pass'), (b'12th Pass', b'12th Pass'), (b'10th + ITI', b'10th + ITI')])),
                ('year_of_passing', models.IntegerField()),
                ('adhar_card_number', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to=b'photos')),
                ('signature', models.ImageField(upload_to=b'signatures')),
                ('left_thumb_impression', models.ImageField(upload_to=b'thumb_impressions')),
                ('courses', models.ManyToManyField(to='students_786ms.Course')),
                ('user', models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='studenttoken',
            name='by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
