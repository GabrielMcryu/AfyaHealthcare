from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile, DoctorProfile, Appointment

class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    YEARS= [x for x in range(1940,2021)]

    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    birth_date = forms.DateField(label='What is your birth date', widget=forms.SelectDateWidget(years=YEARS), required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'gender', 'birth_date']

class UpdateUserForm(UserChangeForm):

    password = None
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UpdateUserProfileForm(ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    YEARS= [x for x in range(1940,2021)]

    phone = forms.CharField(required=True)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    birth_date = forms.DateField(label='What is your birth date', widget=forms.SelectDateWidget(years=YEARS), required=True)

    class Meta:
        model = UserProfile
        fields = ['phone', 'gender', 'birth_date']

class UpdateDoctorProfileForm(ModelForm):
    SPECIALIZATION_CHOICES = [
        ('Dermatology', 'Dermatology'),
        ('Family Medicine', 'Family Medicine'),
        ('Internal Medicine', 'Internal Medicine'),
        ('Neurosurgery', 'Neurosurgery'),
        ('Gynaecology', 'Gynaecology'),
        ('Oncology', 'Oncology'),
        ('Paediatrics', 'Paediatrics'),
        ('Psychiatry', 'Psychiatry'),
        ('Urology', 'Urology'),
        ('Public Health', 'Public Health'),
    ]

    specialization = forms.CharField(label='Choose Specialization', widget=forms.Select(choices=SPECIALIZATION_CHOICES), required=True)
    biography = forms.Textarea()

    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'county', 'biography']

class BookAppointmentForm(ModelForm):
    symptoms = forms.Textarea()

    class Meta:
        model = Appointment
        fields = ['symptoms']

class ApproveAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Approved', 'Approved'),
    ]
    YEARS= [x for x in range(2022,2040)]


    appointment_date = forms.DateField(label='Enter Date', widget=forms.SelectDateWidget(years=YEARS),required=True)
    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'status']

class RejectAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Rejected', 'Rejected')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']

class CompleteAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Completed', 'Completed')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']

class CancelAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Cancelled', 'Cancelled')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']