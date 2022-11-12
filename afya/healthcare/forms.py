from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile

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
