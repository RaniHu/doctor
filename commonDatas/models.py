# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Bingli(models.Model):
    patientid = models.CharField(max_length=50, blank=True, null=True)
    bingliid = models.CharField(primary_key=True, max_length=50)
    hospital = models.CharField(max_length=50, blank=True, null=True)
    departments = models.CharField(max_length=50, blank=True, null=True)
    doctorname = models.CharField(max_length=10, blank=True, null=True)
    visitingtime = models.CharField(max_length=50, blank=True, null=True)
    symptom = models.CharField(max_length=1000, blank=True, null=True)
    nowcase = models.CharField(max_length=1000, blank=True, null=True)
    passcase = models.CharField(max_length=1000, blank=True, null=True)
    healthcheck = models.CharField(max_length=1000, blank=True, null=True)
    othercheck = models.CharField(max_length=1000, blank=True, null=True)
    diagnose = models.CharField(max_length=1000, blank=True, null=True)
    treatadvise = models.CharField(max_length=1000, blank=True, null=True)
    doctoradvise = models.CharField(max_length=1000, blank=True, null=True)
    informnurse = models.CharField(max_length=10, blank=True, null=True)
    observation = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bingli'


class Bingliattachment(models.Model):
    bingliid = models.CharField(primary_key=True, max_length=50)
    imageid = models.CharField(max_length=50, blank=True, null=True)
    imagepath = models.CharField(max_length=100, blank=True, null=True)
    imagesize = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bingliattachment'


class Docpersonalinfo(models.Model):
    userid = models.CharField(primary_key=True, max_length=50)
    userimage = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    usersex = models.CharField(max_length=2, blank=True, null=True)
    userbirth = models.CharField(max_length=20, blank=True, null=True)
    usertel = models.CharField(max_length=30, blank=True, null=True)
    userdepart = models.CharField(max_length=100, blank=True, null=True)
    userhospital = models.CharField(max_length=100, blank=True, null=True)
    userposition = models.CharField(max_length=30, blank=True, null=True)
    useremail = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docpersonalinfo'


class Drugexpense(models.Model):
    bingliid = models.CharField(primary_key=True, max_length=50)
    drugname = models.CharField(max_length=100, blank=True, null=True)
    drugconsumption = models.CharField(max_length=10, blank=True, null=True)
    drugoneprice = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drugexpense'


class Feibingli(models.Model):
    improved = models.CharField(max_length=5000, blank=True, null=True)
    unimproved = models.CharField(max_length=5000, blank=True, null=True)
    writenote = models.CharField(max_length=5000, blank=True, null=True)
    ordernumberid = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'feibingli'


class Patientpersonalinfo(models.Model):
    patientid = models.CharField(primary_key=True, max_length=50)
    patientsex = models.CharField(max_length=2, blank=True, null=True)
    patientname = models.CharField(max_length=10, blank=True, null=True)
    patientaddress = models.CharField(max_length=100, blank=True, null=True)
    patienttel = models.CharField(max_length=20, blank=True, null=True)
    patientemail = models.CharField(max_length=20, blank=True, null=True)
    patientidcard = models.CharField(max_length=20, blank=True, null=True)
    patientmedicalcard = models.CharField(max_length=20, blank=True, null=True)
    patientbirth = models.CharField(max_length=20, blank=True, null=True)
    familyid = models.CharField(max_length=20, blank=True, null=True)
    patientimage = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patientpersonalinfo'


class PollsUsertable(models.Model):
    userid = models.CharField(max_length=30)
    usertel = models.CharField(max_length=30)
    useremail = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    userpassword = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'polls_usertable'


class Prescription(models.Model):
    bingliid = models.CharField(primary_key=True, max_length=50)
    feibie = models.CharField(max_length=50, blank=True, null=True)
    menzhennumber = models.CharField(max_length=50, blank=True, null=True)
    examine = models.CharField(max_length=50, blank=True, null=True)
    distribution = models.CharField(max_length=50, blank=True, null=True)
    check = models.CharField(max_length=50, blank=True, null=True)
    medicine = models.CharField(max_length=50, blank=True, null=True)
    drugtotalprice = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'


class UserlogininUsertable(models.Model):
    userid = models.CharField(max_length=30)
    usertel = models.CharField(max_length=30)
    useremail = models.CharField(max_length=30)
    username = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'userloginin_usertable'


class Unioncomment(models.Model):
    contentid = models.AutoField(primary_key=True)
    contentnum = models.CharField(max_length=50, blank=True, null=True)
    commenttext = models.CharField(max_length=1000, blank=True, null=True)
    commentpersonid = models.CharField(max_length=50, blank=True, null=True)
    commenttime = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unioncomment'


class Uniondetail(models.Model):
    detailid = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=50, blank=True, null=True)
    contenttext = models.CharField(max_length=10000, blank=True, null=True)
    sendtime = models.CharField(max_length=50, blank=True, null=True)
    contentimg = models.CharField(max_length=500, blank=True, null=True)
    contentnum = models.CharField(max_length=50, blank=True, null=True)
    pubname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uniondetail'


class Unionmember(models.Model):
    unionnum = models.CharField(max_length=50, blank=True, null=True)
    memberid = models.CharField(max_length=50, blank=True, null=True)
    unionmemberid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'unionmember'


class Unionname(models.Model):
    unionnum = models.CharField(max_length=50, blank=True, null=True)
    unionname = models.CharField(max_length=50, blank=True, null=True)
    unionnumid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'unionname'


class Unionoutline(models.Model):
    unionnum = models.CharField(max_length=50, blank=True, null=True)
    contentnum = models.CharField(max_length=50, blank=True, null=True)
    contenttype = models.CharField(max_length=50, blank=True, null=True)
    jurisdiction = models.CharField(max_length=50, blank=True, null=True)
    outlineid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'unionoutline'


