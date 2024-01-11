from django.db import models
class Service(models.Model):
    name  = models.CharField(max_length=50,null=True)
    section = models.CharField(max_length=50, null=True) 
  
# Create your models here.
    