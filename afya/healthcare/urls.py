from django.urls import path
from . import views

app_name = 'healthcare'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('register/', views.registerView, name='register'),
    path('finish/', views.finishView, name='finish'),
    path('dashboard/', views.dashBoardView, name='dashboard'),
    path('region/', views.regionView, name='region'),
    path('doctors/<int:id>', views.all_doctors_view, name='all_doctors_view'),
    path('doctor/<int:id>', views.doctorView, name='doctor'),
    path('user_profile/', views.updateUserProfileView, name='user_profile'),
    path('doctor_profile/', views.updateDoctorProfileView, name='doctor_profile'),
    path('patient_appointments/', views.patientAppointmentsView, name='patient_appointments'),
]