from django.db import models
from django.contrib import admin
from commonDatas.models import Docpersonalinfo
# Create your models here.


class UserTable(models.Model):
      userid = models.CharField(max_length=30)
      usertel = models.CharField(max_length=30)
      useremail = models.CharField(max_length=30)
      username = models.CharField(max_length=30)
      def __str__(self):             
         return self.username
     
class UserCssTable(admin.ModelAdmin):
        list_display = ('username','useremail')
