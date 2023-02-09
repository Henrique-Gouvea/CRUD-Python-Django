from django.db import models

# Create your models here.

class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=500)
    UserPassword = models.CharField(max_length=500)
    UserEmail = models.EmailField(max_length=500)