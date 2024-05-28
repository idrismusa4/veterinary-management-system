import re
from unicodedata import category
from django.db import models
from hospDoctor.models import Doctor
from hospPatient.models import Patient
# Create your models here.
class Appointment(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    )
    
    purpose =  models.CharField(max_length=100,default='CHECKUP')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f'{self.patient.user.username} - {self.date} - {self.time}'

class Session(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()


    def __str__(self):
        return f'{self.patient.user.username} - {self.date}'


class Admin(models.Model):
    first_name =  models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)    

class Inventory(models.Model):
    name =  models.CharField(max_length=100)
    quantity =  models.IntegerField()
    price =  models.FloatField(default=2500.00)
    category = models.CharField(max_length=100, default='Medicine')
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('OUT OF STOCK', 'Out of Stock'),
        ('REFILL SOON', 'Refill Soon'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AVAILABLE')


    def __str__(self):
        return f'{self.name} - {self.quantity} - {self.price} - {self.status}'
    