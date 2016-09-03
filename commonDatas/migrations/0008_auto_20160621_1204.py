# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0007_auto_20160620_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
