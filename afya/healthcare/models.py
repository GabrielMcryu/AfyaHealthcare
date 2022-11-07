from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    Gender_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (Gender_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('Phone', max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=Gender_MALE)
    birth_date = models.DateField(null=True)

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255, null=True)
    county = models.CharField(max_length=255, null=True)
    biography = models.TextField(null=True)

class Appointment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(null=True)
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)