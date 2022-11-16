from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    Gender_MALE = 'Male'
    GENDER_FEMALE = 'Female'

    GENDER_CHOICES = [
        (Gender_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField('Phone', max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=Gender_MALE)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name


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
    has_schedule = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

class Appointment(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'
    STATUS_COMPLETED = 'Completed'
    STATUS_CANCELLED = 'Cancelled'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    symptoms = models.TextField(null=True)
    appointment_date = models.DateField(null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=STATUS_PENDING)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_info')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name = 'user_info')

    def __str__(self):
        return f'Appointment {self.created_at}'

class Schedule(models.Model):
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    doctor = models.OneToOneField(DoctorProfile, on_delete=models.CASCADE)
    monday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    tuesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    wednesday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    thursday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    friday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    saturday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)
    sunday = models.CharField(max_length=255, choices=AVAILABILITY_CHOICES)


