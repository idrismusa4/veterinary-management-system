from django.db import models



class Hospuser(models.Model):
    first_name =  models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    