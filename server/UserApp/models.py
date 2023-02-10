from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)

    class Meta:
        db_table = 'users'