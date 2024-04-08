from django.db import models
from hospAuth.models import Hospuser
# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(Hospuser, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
