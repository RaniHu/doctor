# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0002_unioncomment_uniondetail_unionmember_unionname_unionoutline'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotologuePhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.CharField(max_length=100)),
                ('date_taken', models.DateTimeField(null=True, blank=True)),
                ('view_count', models.IntegerField()),
                ('crop_from', models.CharField(max_length=10)),
                ('slug', models.CharField(unique=True, max_length=250)),
                ('caption', models.TextField()),
                ('date_added', models.DateTimeField()),
                ('is_public', models.IntegerField()),
            ],
            options={
                'db_table': 'photologue_photo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PhotologuePhotoeffect',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('description', models.TextField()),
                ('transpose_method', models.CharField(max_length=15)),
                ('color', models.FloatField()),
                ('brightness', models.FloatField()),
                ('contrast', models.FloatField()),
                ('sharpness', models.FloatField()),
                ('filters', models.CharField(max_length=200)),
                ('reflection_size', models.FloatField()),
                ('reflection_strength', models.FloatField()),
                ('background_color', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'photologue_photoeffect',
                'managed': False,
            },
        ),
    ]
