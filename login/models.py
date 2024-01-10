from django.db import models


class Login(models.Model):
    name = models.TextField(max_length=50)
    password = models.TextField(max_length = 50)
# Create your models here.
