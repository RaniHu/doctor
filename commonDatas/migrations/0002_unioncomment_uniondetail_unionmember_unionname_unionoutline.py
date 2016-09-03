# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unioncomment',
            fields=[
                ('contentid', models.AutoField(primary_key=True, serialize=False)),
                ('contentnum', models.CharField(blank=True, max_length=50, null=True)),
                ('commenttext', models.CharField(blank=True, max_length=1000, null=True)),
                ('commentpersonid', models.CharField(blank=True, max_length=50, null=True)),
                ('commenttime', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'unioncomment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Uniondetail',
            fields=[
                ('detailid', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('contenttext', models.CharField(blank=True, max_length=10000, null=True)),
                ('sendtime', models.CharField(blank=True, max_length=50, null=True)),
                ('contentimg', models.CharField(blank=True, max_length=500, null=True)),
                ('contentnum', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'uniondetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unionmember',
            fields=[
                ('unionnum', models.CharField(blank=True, max_length=50, null=True)),
                ('memberid', models.CharField(blank=True, max_length=50, null=True)),
                ('unionmemberid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'unionmember',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unionname',
            fields=[
                ('unionnum', models.CharField(blank=True, max_length=50, null=True)),
                ('unionname', models.CharField(blank=True, max_length=50, null=True)),
                ('unionnumid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'unionname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Unionoutline',
            fields=[
                ('unionnum', models.CharField(blank=True, max_length=50, null=True)),
                ('contentnum', models.CharField(blank=True, max_length=50, null=True)),
                ('contenttype', models.CharField(blank=True, max_length=50, null=True)),
                ('jurisdiction', models.CharField(blank=True, max_length=50, null=True)),
                ('outlineid', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'unionoutline',
                'managed': False,
            },
        ),
    ]
