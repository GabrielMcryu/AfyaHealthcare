from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import *
from .models import UserProfile, Region, DoctorProfile, Appointment

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
            return render(request, 'healthcare/dashboard.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def indexView(request):
    return render(request, 'healthcare/index.html')

def finishView(request):
    return render(request, 'healthcare/finish.html')

@login_required(login_url='/login')
def dashBoardView(request):
    return render(request, 'healthcare/dashboard.html')

@login_required(login_url='/login')
def regionView(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}

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

@login_required(login_url='/login')
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
    doctor_id = id
    user_data = request.user
    user = UserProfile.objects.get(user=user_data)
    doctor = DoctorProfile.objects.get(id=doctor_id)
    form = BookAppointmentForm(request.POST)
    if form.is_valid():
        symptoms = form.cleaned_data.get('symptoms')
        appointment_data = Appointment.objects.create(symptoms=symptoms, user=user, doctor=doctor)
        appointment_data.save()
        return render(request, 'healthcare/dashboard.html')
    else:
        form = BookAppointmentForm()
    context = {'form': form}
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
    appointment_data = Appointment.objects.get(id=id)
    form = ApproveAppointmentForm(request.POST or None, instance=appointment_data)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    context = {'form': form}
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
