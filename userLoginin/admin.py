from django.contrib import admin
from .models import UserTable
from .models import UserCssTable
# Register your models here.
admin.site.register(UserTable,UserCssTable)
