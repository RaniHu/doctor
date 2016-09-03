# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('userid', models.CharField(max_length=30)),
                ('usertel', models.CharField(max_length=30)),
                ('useremail', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
