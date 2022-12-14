from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'healthcare'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('register/', views.registerView, name='register'),
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
    path('create_schedule/', views.createScheduleView, name='create_schedule'),
    path('update_schedule/', views.updateScheduleView, name='update_schedule'),
    path('careers/', views.doctorApplicationView, name='careers'),
    path('update_appointment/<int:id>', views.updateAppointmentView, name='update_appointment'),
    path('update_patient_appointment/<int:id>', views.updatePatientAppointmentView, name='update_patient_appointment'),
    path('our_services/', views.ourServicesView, name='our_services'),
    path('counties/', views.countiesView, name='counties'),
    path('county_doctors/<int:id>', views.countyDoctorView, name='county_doctors'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='password'),
    path('password/', views.PasswordsChangeView.as_view(), name='password'),
    path('reset_password/', views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', views.resetPasswordSentView, name="reset_password_done"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', views.resetPasswordCompleteView, name="password_reset_complete")
]