# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publishedDate',
            field=models.DateField(default=datetime.date(2014, 9, 18)),
            preserve_default=False,
        ),
    ]
