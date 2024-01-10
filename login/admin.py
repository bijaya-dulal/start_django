from django.contrib import admin
from login.models import Login

class LoginAdmin(admin.ModelAdmin):
    list_display = ('name','password','id')
# Register your models here. 
admin.site.register(Login,LoginAdmin)