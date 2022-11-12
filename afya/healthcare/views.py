from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .forms import UserRegistrationForm, UpdateUserForm, UpdateUserProfileForm, UpdateDoctorProfileForm
from .models import UserProfile, Region, DoctorProfile

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
    context = {'doctor_list': doctor_list}
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

@login_required(login_url='/login')
@permission_required('healthcare.view_region', raise_exception=True)
def patientAppointmentsView(request):
    return render(request, 'healthcare/patient_appointments.html')
