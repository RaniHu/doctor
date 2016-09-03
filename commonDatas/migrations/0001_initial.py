# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bingli',
            fields=[
                ('patientid', models.CharField(blank=True, max_length=50, null=True)),
                ('bingliid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('hospital', models.CharField(blank=True, max_length=50, null=True)),
                ('departments', models.CharField(blank=True, max_length=50, null=True)),
                ('doctorname', models.CharField(blank=True, max_length=10, null=True)),
                ('visitingtime', models.CharField(blank=True, max_length=50, null=True)),
                ('symptom', models.CharField(blank=True, max_length=1000, null=True)),
                ('nowcase', models.CharField(blank=True, max_length=1000, null=True)),
                ('passcase', models.CharField(blank=True, max_length=1000, null=True)),
                ('healthcheck', models.CharField(blank=True, max_length=1000, null=True)),
                ('othercheck', models.CharField(blank=True, max_length=1000, null=True)),
                ('diagnose', models.CharField(blank=True, max_length=1000, null=True)),
                ('treatadvise', models.CharField(blank=True, max_length=1000, null=True)),
                ('doctoradvise', models.CharField(blank=True, max_length=1000, null=True)),
                ('informnurse', models.CharField(blank=True, max_length=10, null=True)),
                ('observation', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'bingli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bingliattachment',
            fields=[
                ('bingliid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('imageid', models.CharField(blank=True, max_length=50, null=True)),
                ('imagepath', models.CharField(blank=True, max_length=100, null=True)),
                ('imagesize', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'bingliattachment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Docpersonalinfo',
            fields=[
                ('userid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('userimage', models.CharField(blank=True, max_length=100, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('usersex', models.CharField(blank=True, max_length=2, null=True)),
                ('userbirth', models.CharField(blank=True, max_length=20, null=True)),
                ('usertel', models.CharField(blank=True, max_length=20, null=True)),
                ('userdepart', models.CharField(blank=True, max_length=100, null=True)),
                ('userhospital', models.CharField(blank=True, max_length=100, null=True)),
                ('userposition', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'docpersonalinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Drugexpense',
            fields=[
                ('bingliid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('drugname', models.CharField(blank=True, max_length=100, null=True)),
                ('drugconsumption', models.CharField(blank=True, max_length=10, null=True)),
                ('drugoneprice', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'drugexpense',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feibingli',
            fields=[
                ('improved', models.CharField(blank=True, max_length=5000, null=True)),
                ('unimproved', models.CharField(blank=True, max_length=5000, null=True)),
                ('writenote', models.CharField(blank=True, max_length=5000, null=True)),
                ('ordernumberid', models.CharField(serialize=False, max_length=50, primary_key=True)),
            ],
            options={
                'db_table': 'feibingli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patientpersonalinfo',
            fields=[
                ('patientid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('patientsex', models.CharField(blank=True, max_length=2, null=True)),
                ('patientname', models.CharField(blank=True, max_length=10, null=True)),
                ('patientaddress', models.CharField(blank=True, max_length=100, null=True)),
                ('patienttel', models.CharField(blank=True, max_length=20, null=True)),
                ('patientemail', models.CharField(blank=True, max_length=20, null=True)),
                ('patientidcard', models.CharField(blank=True, max_length=20, null=True)),
                ('patientmedicalcard', models.CharField(blank=True, max_length=20, null=True)),
                ('patientbirth', models.CharField(blank=True, max_length=20, null=True)),
                ('familyid', models.CharField(blank=True, max_length=20, null=True)),
                ('patientimage', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'patientpersonalinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PollsUsertable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('userid', models.CharField(max_length=30)),
                ('usertel', models.CharField(max_length=30)),
                ('useremail', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('userpassword', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'polls_usertable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('bingliid', models.CharField(serialize=False, max_length=50, primary_key=True)),
                ('feibie', models.CharField(blank=True, max_length=50, null=True)),
                ('menzhennumber', models.CharField(blank=True, max_length=50, null=True)),
                ('examine', models.CharField(blank=True, max_length=50, null=True)),
                ('distribution', models.CharField(blank=True, max_length=50, null=True)),
                ('check', models.CharField(blank=True, max_length=50, null=True)),
                ('medicine', models.CharField(blank=True, max_length=50, null=True)),
                ('drugtotalprice', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'prescription',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserlogininUsertable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('userid', models.CharField(max_length=30)),
                ('usertel', models.CharField(max_length=30)),
                ('useremail', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'userloginin_usertable',
                'managed': False,
            },
        ),
    ]
