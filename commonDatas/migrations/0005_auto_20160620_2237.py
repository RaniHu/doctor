# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0004_auto_20160620_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='person',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
