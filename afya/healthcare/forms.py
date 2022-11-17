from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile, DoctorProfile, Appointment, Schedule

class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    YEARS= [x for x in range(1940,2021)]
    # years=YEARS

    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    # birth_date = forms.DateField(label='What is your birth date', widget=forms.SelectDateWidget(attrs={'class':'birth_date'}), required=True)
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class':'birth_date',}), required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'gender', 'birth_date']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['birth_date'].widget.attrs.update({'id': 'birth_date'})

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
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class':'birth_date',}), required=True)

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
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date',}), required=True)
    symptoms = forms.Textarea()

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'symptoms']

class ApproveAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Approved', 'Approved'),
    ]
    YEARS= [x for x in range(2022,2040)]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    
    class Meta:
        model = Appointment
        fields = ['status']

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

class CreateScheduleForm(ModelForm):
    STATUS_CHOICE = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]

    monday = forms.CharField(label='Monday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    tuesday = forms.CharField(label='Tuesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    wednesday = forms.CharField(label='Wednesday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    thursday = forms.CharField(label='Thursday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    friday = forms.CharField(label='Friday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    saturday = forms.CharField(label='Saturday', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    sunday = forms.CharField(label='Sunday', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']