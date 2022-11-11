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

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField('Phone', max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=Gender_MALE)
    birth_date = models.DateField(null=True)


class Region(models.Model):
    COUNTY_NAIROBI = 'Nairobi'
    COUNTY_MOMBASA = 'Mombasa'

    COUNTY_CHOICES = [
        (COUNTY_NAIROBI, 'Nairobi'),
        (COUNTY_MOMBASA, 'Mombasa'),
    ]

    county = models.CharField(max_length=255, choices=COUNTY_CHOICES, null=True)

    def __str__(self):
        return self.county

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profiles')
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES , null=True)
    county = models.ForeignKey(Region, on_delete=models.CASCADE)
    biography = models.TextField(null=True)

class Appointment(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(null=True)
    appontment_date = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_PENDING)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_info')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_info')

