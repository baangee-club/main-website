# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_baangee', '0012_contactperson'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactperson',
            name='image',
            field=models.ImageField(default='', upload_to=b'contact_persons'),
            preserve_default=False,
        ),
    ]
