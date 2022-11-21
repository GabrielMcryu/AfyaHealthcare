from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile, DoctorProfile, Appointment, Schedule, DoctorApplication

class UserRegistrationForm(UserCreationForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    YEARS= [x for x in range(1940,2021)]
    # years=YEARS

    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password'}),
        )
    password2 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Password Again'}),
        )
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Enter your phone number'}))
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES, attrs={'class': 'input-field'}), required=True)
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field', 'id':'birth_date', 'placeholder': 'Enter birth date', 'autocomplete': 'off'}), required=True)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'gender', 'birth_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Last Name'})

class UpdateUserForm(UserChangeForm):
    password = None
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Username'})
    )
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Enter Last Name'})

class UpdateUserProfileForm(ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    YEARS= [x for x in range(1940,2021)]

    phone = forms.CharField(required=True)
    gender = forms.CharField(label='Choose your Gender', widget=forms.Select(choices=GENDER_CHOICES), required=True)
    birth_date = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field', 'id': 'birth_date'}), required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs.update({'class': 'input-field', 'placeholder': 'Phone number'})
        self.fields['gender'].widget.attrs.update({'class': 'input-field',})

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].widget.attrs.update({'class': 'input-field'})
        self.fields['county'].widget.attrs.update({'class': 'input-field',})
        self.fields['biography'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})

class BookAppointmentForm(ModelForm):
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field', 'placeholder': 'Enter Date', 'autocomplete': 'off'}), required=True)
    symptoms = forms.Textarea()

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'symptoms']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})

class ApproveAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Approved', 'Approved'),
    ]
    YEARS= [x for x in range(2022,2040)]

    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field', 'autocomplete': 'off'}), required=True)
    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)
    
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})

class RejectAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Rejected', 'Rejected')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})

class CompleteAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Completed', 'Completed')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})

class CancelAppointmentForm(ModelForm):
    STATUS_CHOICE = [
        ('Cancelled', 'Cancelled')
    ]

    status = forms.CharField(label='Status', widget=forms.Select(choices=STATUS_CHOICE), required=True)

    class Meta:
        model = Appointment
        fields = ['status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'input-field'})
    
class UpdateAppointmentForm(ModelForm):
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field'}), required=True)
    symptoms = forms.Textarea()

    class Meta:
        model = Appointment
        fields = ['appointment_date', 'symptoms']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['symptoms'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})

class UpdatePatientAppointmentForm(ModelForm):
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'id':'appointment_date', 'class': 'input-field'}), required=True)

    class Meta:
        model = Appointment
        fields = ['appointment_date']

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['monday'].widget.attrs.update({'class': 'input-field'})
        self.fields['tuesday'].widget.attrs.update({'class': 'input-field'})
        self.fields['wednesday'].widget.attrs.update({'class': 'input-field'})
        self.fields['thursday'].widget.attrs.update({'class': 'input-field'})
        self.fields['friday'].widget.attrs.update({'class': 'input-field'})
        self.fields['saturday'].widget.attrs.update({'class': 'input-field'})
        self.fields['sunday'].widget.attrs.update({'class': 'input-field'})

class DoctorApplicationForm(ModelForm):
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

    STATUS_CHOICE = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    specialization = forms.CharField(label='Choose Specialization', widget=forms.Select(choices=SPECIALIZATION_CHOICES), required=True)
    biography = forms.Textarea()

    class Meta:
        model = DoctorApplication
        fields = ['specialization', 'county', 'biography']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].widget.attrs.update({'class': 'input-field'})
        self.fields['county'].widget.attrs.update({'class': 'input-field',})
        self.fields['biography'].widget.attrs.update({'class': 'input-field', 'cols': '30', 'rows': '10'})