from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=15)
    address = models.TextField()
    bed_num = models.ForeignKey("Bed", on_delete=models.CASCADE)
    enfermedad=models.ForeignKey("Enfermedad",on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, null=True)
    doctors_notes = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
        
class Bed(models.Model):
    bed_number = models.CharField(max_length=50)
    occupied = models.BooleanField()
    def __str__(self):
        return self.bed_number


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Enfermedad(models.Model):
    name = models.CharField(max_length=50)
    description=models.TextField()
    def __str__(self):
        return self.name



