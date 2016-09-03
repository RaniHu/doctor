# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0008_auto_20160621_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailcomment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('userid', models.CharField(blank=True, null=True, max_length=50)),
                ('contenttext', models.CharField(blank=True, null=True, max_length=10000)),
                ('sendtime', models.CharField(blank=True, null=True, max_length=50)),
                ('contentimg', models.CharField(blank=True, null=True, max_length=500)),
                ('contentnum', models.CharField(blank=True, null=True, max_length=50)),
                ('pubname', models.CharField(blank=True, null=True, max_length=20)),
                ('commenttext', models.CharField(blank=True, null=True, max_length=1000)),
                ('commentpersonid', models.CharField(blank=True, null=True, max_length=50)),
                ('commenttime', models.CharField(blank=True, null=True, max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'Detailcomment',
            },
        ),
    ]
