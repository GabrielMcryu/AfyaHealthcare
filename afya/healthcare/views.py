from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import UserProfile, Region, DoctorProfile, Appointment, Schedule
from .emails import sendEmail
from .myfunctions import appointment_availability

# Create your views here.
def registerView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone')
            gender = form.cleaned_data.get('gender')
            birth_date = form.cleaned_data.get('birth_date')

            user = User.objects.get(username=username)
            user_data = UserProfile.objects.create(user=user, phone=phone, gender=gender, birth_date=birth_date)
            user_data.save()
            return render(request, 'healthcare/index.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def indexView(request):
    return render(request, 'healthcare/index.html')

@login_required(login_url='/login')
def dashBoardView(request):
    user_data = request.user
    check_doctor = DoctorProfile.objects.filter(user=user_data).count()
    check_application = DoctorApplication.objects.filter(user=user_data).count()
    if check_doctor > 0:
        doctor_data = DoctorProfile.objects.get(user=user_data)
        context = {
            'doctor_data': doctor_data,
            'check_application': check_application,
            'check_doctor': check_doctor,
        }
    else:
        context = {
            'check_application': check_application,
            'check_doctor': check_doctor,
        }
    return render(request, 'healthcare/dashboard.html', context=context)

@login_required(login_url='/login')
def regionView(request):
    all_regions = Region.objects.all()
    my_data = [1, 2, 3]
    context = {
        'all_regions': all_regions,
        'my_data': my_data,
        }

    return render(request, 'healthcare/region.html', context=context)

@login_required(login_url='/login')
def all_doctors_view(request, id):
    region_id = id
    doctor_list = DoctorProfile.objects.filter(county=region_id).order_by('specialization')
    user_session = request.user
    user = UserProfile.objects.get(user=user_session)
    check_pending = Appointment.objects.filter(user=user, status='Pending').count()
    check_approved = Appointment.objects.filter(user=user, status='Approved').count()
    check_appointments = check_pending + check_approved
    context = {
        'doctor_list': doctor_list, 
        'check_appointments': check_appointments
        }
    return render(request, 'healthcare/view_doctors.html', context=context)

def doctorView(request, id):
    doctor_data = DoctorProfile.objects.get(id=id)
    context = {'doctor_data': doctor_data}
    return render(request, 'healthcare/view_doctor.html', context=context)

@login_required(login_url='/login')
def updateUserProfileView(request):
    current_user = request.user
    user_profile = UserProfile.objects.get(user=current_user.id)
    form = UpdateUserForm(request.POST or None, instance=current_user)
    user_form = UpdateUserProfileForm(request.POST or None, instance=user_profile)
    if form.is_valid() and user_form.is_valid():
        form.save()
        user_form.save()
        return redirect('/dashboard/')
    context = {'form': form, 'user_form': user_form}
    return render(request, 'healthcare/user_profile.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def updateDoctorProfileView(request):
    current_user = request.user
    doctor_profile = DoctorProfile.objects.get(user=current_user.id)
    form = UpdateDoctorProfileForm(request.POST or None, instance=doctor_profile)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form }
    return render(request, 'healthcare/doctor_profile.html', context=context)

@login_required(login_url='\login')
def bookAppointmentView(request, id):
    schedule_data = {}
    doctor_id = id
    user_data = request.user
    user = UserProfile.objects.get(user=user_data)
    doctor = DoctorProfile.objects.get(id=doctor_id)
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
        appointment_date = form.cleaned_data.get('appointment_date')
        symptoms = form.cleaned_data.get('symptoms')
        appointment_data = Appointment.objects.create(appointment_date=appointment_date, symptoms=symptoms, user=user, doctor=doctor)
        appointment_data.save()
        return render(request, 'healthcare/dashboard.html')
    else:
        form = BookAppointmentForm()
    doctor_schedule = Schedule.objects.get(doctor=doctor)
    schedule_data['monday'] = doctor_schedule.monday
    schedule_data['tuesday'] = doctor_schedule.tuesday
    schedule_data['wednesday'] = doctor_schedule.wednesday
    schedule_data['thursday'] = doctor_schedule.thursday
    schedule_data['friday'] = doctor_schedule.friday
    schedule_data['saturday'] = doctor_schedule.saturday
    schedule_data['sunday'] = doctor_schedule.sunday
    filtered_schedule = appointment_availability(schedule_data)
    context = {'form': form, 'filtered_schedule': filtered_schedule}
    return render(request, 'healthcare/book_appointment.html', context=context)

@login_required(login_url='\login')
def viewAppointmentsView(request):
    user_session = request.user
    user_profile = UserProfile.objects.get(user=user_session)
    pending_appointments = Appointment.objects.filter(user=user_profile, status='Pending')
    approved_appointments = Appointment.objects.filter(user=user_profile, status='Approved')
    rejected_appointments = Appointment.objects.filter(user=user_profile, status='Rejected')
    context = {
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'rejected_appointments': rejected_appointments,
        }
    return render(request, 'healthcare/view_appointments.html', context=context)

@login_required(login_url='\login')
def viewAppointmentView(request, id):
    appointment_data = Appointment.objects.get(id=id)
    context = {'appointment_data': appointment_data}
    return render(request, 'healthcare/view_appointment.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def patientAppointmentsView(request):
    user = request.user
    doctor = DoctorProfile.objects.get(user=user)
    pending_appointments = Appointment.objects.filter(doctor=doctor, status='Pending')
    approved_appointments = Appointment.objects.filter(doctor=doctor, status='Approved')
    rejected_appointments = Appointment.objects.filter(doctor=doctor, status='Rejected')
    context = {
        'pending_appointments': pending_appointments,
        'approved_appointments': approved_appointments,
        'rejected_appointments': rejected_appointments,
    }
    return render(request, 'healthcare/patient_appointments.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def patientAppointmentView(request, id):
    appointment_data = Appointment.objects.get(id=id)
    context = {'appointment_data': appointment_data}
    return render(request, 'healthcare/patient_appointment.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def approveAppointment(request, id):
    email_header = 'Your appointment has been approved!'
    appointment_data = Appointment.objects.get(id=id)
    user_email = appointment_data.user.user.email
    doctor_data = {}
    doctor_first_name = appointment_data.doctor.user.first_name
    doctor_last_name = appointment_data.doctor.user.last_name
    doctor_specialization = appointment_data.doctor.specialization
    symptoms = appointment_data.symptoms
    doctor_data['first_name'] = doctor_first_name
    doctor_data['last_name'] = doctor_last_name
    doctor_data['specialization'] = doctor_specialization
    form = ApproveAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        date = form.cleaned_data.get('appointment_date')
        form.save()
        sendEmail(user_email, email_header, doctor_data, symptoms, date)
        return redirect('/dashboard/')
    schedule_data = {}
    user = request.user
    doctor = DoctorProfile.objects.get(user=user)
    doctor_schedule = Schedule.objects.get(doctor=doctor)
    schedule_data['monday'] = doctor_schedule.monday
    schedule_data['tuesday'] = doctor_schedule.tuesday
    schedule_data['wednesday'] = doctor_schedule.wednesday
    schedule_data['thursday'] = doctor_schedule.thursday
    schedule_data['friday'] = doctor_schedule.friday
    schedule_data['saturday'] = doctor_schedule.saturday
    schedule_data['sunday'] = doctor_schedule.sunday
    filtered_schedule = appointment_availability(schedule_data)
    context = {'form': form, 'filtered_schedule': filtered_schedule}
    return render(request, 'healthcare/approve.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def rejectAppointment(request, id):
    appointment_data = Appointment.objects.get(id=id)
    form = RejectAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form}
    return render(request, 'healthcare/reject.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def completeAppointment(request, id):
    appointment_data = Appointment.objects.get(id=id)
    form = CompleteAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form}
    return render(request, 'healthcare/finish.html', context=context)

@login_required(login_url='/login')
def cancelAppointment(request, id):
    appointment_data = Appointment.objects.get(id=id)
    form = CancelAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form}
    return render(request, 'healthcare/cancel.html', context=context)

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def createScheduleView(request):
    user_data = request.user
    doctor_data = DoctorProfile.objects.get(user=user_data)
    if request.method == 'POST':
        form = CreateScheduleForm(request.POST)
        if form.is_valid():
            monday = form.cleaned_data.get('monday')
            tuesday = form.cleaned_data.get('tuesday')
            wednesday = form.cleaned_data.get('wednesday')
            thursday = form.cleaned_data.get('thursday')
            friday = form.cleaned_data.get('friday')
            saturday = form.cleaned_data.get('saturday')
            sunday = form.cleaned_data.get('sunday')
            schedule_data = Schedule.objects.create(doctor=doctor_data, monday=monday, tuesday=tuesday, wednesday=wednesday, thursday=thursday, friday=friday, saturday=saturday, sunday=sunday)
            schedule_data.save()
            doctor_data.has_schedule = True
            doctor_data.save()
            return redirect('/dashboard/')
    else:
        form = CreateScheduleForm()
    return render(request, 'healthcare/create_schedule.html', {'form': form})

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def updateScheduleView(request):
    user_data = request.user
    doctor_data = DoctorProfile.objects.get(user=user_data)
    schedule_data = Schedule.objects.get(doctor=doctor_data)
    form = CreateScheduleForm(request.POST or None, instance=schedule_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form}
    return render(request, 'healthcare/update_schedule.html', context=context)

@login_required(login_url='/login')
def doctorApplicationView(request):
    user_data = request.user
    if request.method == 'POST':
        form = DoctorApplicationForm(request.POST)
        if form.is_valid():
            specialization = form.cleaned_data.get('specialization')
            county = form.cleaned_data.get('county')
            biography = form.cleaned_data.get('biography')
            application_data = DoctorApplication.objects.create(user=user_data, specialization=specialization, county=county, biography=biography)
            application_data.save()
            return redirect('/dashboard/')
    else:
        form = DoctorApplicationForm()
    return render(request, 'healthcare/careers.html', {'form': form})

@login_required(login_url='/login')
def updateAppointmentView(request, id):
    schedule_data = {}
    appointment_data = Appointment.objects.get(id=id)
    doctor = DoctorProfile.objects.get(id=appointment_data.doctor.id)
    form = UpdateAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    doctor_schedule = Schedule.objects.get(doctor=doctor)
    schedule_data['monday'] = doctor_schedule.monday
    schedule_data['tuesday'] = doctor_schedule.tuesday
    schedule_data['wednesday'] = doctor_schedule.wednesday
    schedule_data['thursday'] = doctor_schedule.thursday
    schedule_data['friday'] = doctor_schedule.friday
    schedule_data['saturday'] = doctor_schedule.saturday
    schedule_data['sunday'] = doctor_schedule.sunday
    filtered_schedule = appointment_availability(schedule_data)
    context = {'form': form, 'filtered_schedule': filtered_schedule}
    return render(request, 'healthcare/update_appointment.html', context=context)

@login_required(login_url='/login')
def updatePatientAppointmentView(request, id):
    schedule_data = {}
    appointment_data = Appointment.objects.get(id=id)
    user_data = request.user
    doctor = DoctorProfile.objects.get(user=user_data)
    form = UpdatePatientAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    doctor_schedule = Schedule.objects.get(doctor=doctor)
    schedule_data['monday'] = doctor_schedule.monday
    schedule_data['tuesday'] = doctor_schedule.tuesday
    schedule_data['wednesday'] = doctor_schedule.wednesday
    schedule_data['thursday'] = doctor_schedule.thursday
    schedule_data['friday'] = doctor_schedule.friday
    schedule_data['saturday'] = doctor_schedule.saturday
    schedule_data['sunday'] = doctor_schedule.sunday
    filtered_schedule = appointment_availability(schedule_data)
    context = {'form': form, 'filtered_schedule': filtered_schedule}
    return render(request, 'healthcare/update_patient_appointment.html', context=context)

def ourServicesView(request):
    return render(request, 'healthcare/our_services.html')

def countiesView(request):
    all_regions = Region.objects.all()
    my_data = [1, 2, 3]
    context = {
        'all_regions': all_regions,
        'my_data': my_data,
    }
    return render(request, 'healthcare/counties.html', context=context)

def countyDoctorView(request, id):
    region_id = id
    doctor_list = DoctorProfile.objects.filter(county=region_id).order_by('specialization')
    context = {
        'doctor_list': doctor_list, 
    }
    return render(request, 'healthcare/county_doctor.html', context=context)

