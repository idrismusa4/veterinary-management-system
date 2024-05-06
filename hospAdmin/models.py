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
    PRESCRIPTION_CHOICES = (
        ('paracetamol, ibuprofen', 'Paracetamol, Ibuprofen'),
        ('antibiotics', 'Antibiotics'),
        ('antihistamines', 'Antihistamines'),
        ('antacids', 'Antacids'),
        ('anticoagulants', 'Anticoagulants'),
        ('antidepressants', 'Antidepressants'),
        ('antipsychotics', 'Antipsychotics'),
        ('anesthetics', 'Anesthetics'),
        ('antivirals', 'Antivirals'),
        ('bronchodilators', 'Bronchodilators'),
        ('contraceptives', 'Contraceptives'),
        ('diuretics', 'Diuretics'),
        ('laxatives', 'Laxatives'),
        ('stimulants', 'Stimulants'),
        ('steroids', 'Steroids'),
        ('muscle relaxants', 'Muscle Relaxants'),
        ('narcotics', 'Narcotics'),
        ('sedatives', 'Sedatives'),
        ('tranquilizers', 'Tranquilizers'),
        ('vaccines', 'Vaccines'),
        ('vitamins', 'Vitamins'),
        ('other', 'Other'),
)

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    prescription = models.CharField(max_length=100, choices=PRESCRIPTION_CHOICES, default='paracetamol, ibuprofen')


    def __str__(self):
        return f'{self.patient.user.username} - {self.date}'


class Admin(models.Model):
    first_name =  models.CharField(max_length=100)
    username =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    