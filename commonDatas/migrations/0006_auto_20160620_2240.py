# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonDatas', '0005_auto_20160620_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='书籍名称')),
                ('pubtime', models.DateField(verbose_name='出版时间')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='作者姓名')),
                ('age', models.IntegerField(verbose_name='作者年龄')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='person',
            field=models.ForeignKey(related_name='person_book', to='commonDatas.Person'),
        ),
    ]
