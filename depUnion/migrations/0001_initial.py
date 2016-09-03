# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unioncomment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('contentid', models.CharField(max_length=50)),
                ('commenttext', models.CharField(blank=True, null=True, max_length=1000)),
                ('commentpersonid', models.CharField(blank=True, null=True, max_length=50)),
                ('commenttime', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'db_table': 'unioncomment',
                'managed': False,
            },
        ),
    ]
