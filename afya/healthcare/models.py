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
    S_DERMATOLOGY = 'Dermatology'
    S_FAMILY_MEDICINE = 'Family Medicine'
    S_INTERNAL_MEDICINE = 'Internal Medicine'
    S_NEUROSURGERY = 'Neurosurgery'
    S_GYNAECOLOGY = 'Gynaecology'
    S_ONCOLOGY = 'Oncology'
    S_PAEDIATRICS = 'Paediatrics'
    S_PSYCHIATRY = 'Psychiatry'
    S_UROLOGY = 'Urology'
    S_PUBLIC_HEALTH = 'Public Health'

    SPECIALIZATION_CHOICES = [
        (S_DERMATOLOGY, 'Dermatology'),
        (S_FAMILY_MEDICINE, 'Family Medicine'),
        (S_INTERNAL_MEDICINE, 'Internal Medicine'),
        (S_NEUROSURGERY, 'Neurosurgery'),
        (S_GYNAECOLOGY, 'Gynaecology'),
        (S_ONCOLOGY, 'Oncology'),
        (S_PAEDIATRICS, 'Paediatrics'),
        (S_PSYCHIATRY, 'Psychiatry'),
        (S_UROLOGY, 'Urology'),
        (S_PUBLIC_HEALTH, 'Public Health'),
    ]

    COUNTY_NAIROBI = 'Nairobi'
    COUNTY_MOMBASA = 'Mombasa'

    COUNTY_CHOICES = [
        (COUNTY_NAIROBI, 'Nairobi'),
        (COUNTY_MOMBASA, 'Mombasa'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES , null=True)
    county = models.CharField(max_length=255, choices=COUNTY_CHOICES, null=True)
    biography = models.TextField(null=True)

class Appointment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(null=True)
    doctor_id = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)