from django.db import models
from hospAuth.models import Hospuser
# Create your models here.

class Patient(models.Model):
    user = models.OneToOneField(Hospuser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.user.username
