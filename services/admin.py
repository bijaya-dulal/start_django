from django.contrib import admin
from services.models import Service
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display =('id','name','section')

admin.site.register(Service,ServiceAdmin)