from django.db import models
from commonDatas import *

class Detailcomment(models.Model):
    userid = models.CharField(max_length=50, blank=True, null=True)
    contenttext = models.CharField(max_length=10000, blank=True, null=True)
    sendtime = models.CharField(max_length=50, blank=True, null=True)
    contentimg = models.CharField(max_length=500, blank=True, null=True)
    contentnum = models.CharField(max_length=50, blank=True, null=True)
    pubname = models.CharField(max_length=20, blank=True, null=True)
    commenttext = models.CharField(max_length=1000, blank=True, null=True)
    commentpersonid = models.CharField(max_length=50, blank=True, null=True)
    commenttime = models.CharField(max_length=50, blank=True, null=True)
    class Meta:
         managed = False
         db_table = "detailcomment"