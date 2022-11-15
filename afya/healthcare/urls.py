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
    path('book_appointment/<int:id>', views.bookAppointmentView, name='book_appointment'),
    path('view_appointments/', views.viewAppointmentsView, name='view_appointments'),
    path('view_appointment/<int:id>', views.viewAppointmentView, name='view_appointment'),
    path('patient_appointments/', views.patientAppointmentsView, name='patient_appointments'),
    path('patient_appointment/<int:id>', views.patientAppointmentView, name='patient_appointment'),
    path('approve/<int:id>', views.approveAppointment, name='approve'),
    path('reject/<int:id>',views.rejectAppointment, name='reject'),
    path('complete/<int:id>', views.completeAppointment, name='complete'),
    path('cancel/<int:id>', views.cancelAppointment, name='cancel'),
]