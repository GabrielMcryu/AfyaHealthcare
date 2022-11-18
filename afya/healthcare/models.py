from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.models import Group
from .emails import applicationEmail

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

    def __str__(self):
        return f'Schedule for {self.doctor.user.first_name}'

class DoctorApplication(models.Model):
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

    STATUS_PENDING = 'Pending'
    STATUS_APPROVED = 'Approved'
    STATUS_REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_REJECTED, 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_applications')
    specialization = models.CharField(max_length=50,choices=SPECIALIZATION_CHOICES)
    county = models.ForeignKey(Region, on_delete=models.CASCADE)
    biography = models.TextField(null=True, default='-')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return f'Application for {self.user.first_name}'

    def save(self, *args, **kwargs):
        if self.status == 'Approved':
            doctor_data = DoctorProfile.objects.create(user=self.user, specialization=self.specialization, county=self.county, biography=self.biography)
            doctor_data.save()
            group = Group.objects.get(id=1)
            group.user_set.add(self.user)
            email_header = f'Your application #{self.id} has been Approved'
            email_body = f'Dear Mr/Mrs {self.user.first_name} \n\n Congratulations! your application for being a doctor in afya healthcare has been approved! Kindly log in to set up your account. \n\n Regards,\n Afya Healthcare'
            applicationEmail(self.user.email, email_header, email_body)
        elif self.status == 'Rejected':
            email_header = f'Your application #{self.id} has been Rejected'
            email_body = f'Dear Mr/Mrs {self.user.first_name} \n\n Unfortunately, your application for being a doctor has been rejected. If you still wish to to join us, you can reapply after 3 months. \n\n Regards,\n Afya Healthcare'
            applicationEmail(self.user.email, email_header, email_body)
            return super().delete(*args, **kwargs)
        return super().save(*args, **kwargs)