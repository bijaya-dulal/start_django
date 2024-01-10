from django.db import models
class Service(models.Model):
    name  = models.CharField(max_length=50,)
    section = models.CharField(max_length=50,) 
  
# Create your models here.
    