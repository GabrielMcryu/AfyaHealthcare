from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile, Region, DoctorProfile
from django.urls import reverse

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
            return render(request, 'registration/login.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def finishView(request):
    return render(request, 'healthcare/finish.html')

def dashBoardView(request):
    return render(request, 'healthcare/dashboard.html')

def regionView(request):
    all_regions = Region.objects.all()
    context = {'all_regions': all_regions}

    return render(request, 'healthcare/region.html', context=context)

def all_doctors_view(request, id):
    region_id = id
    print(id)
    doctor_list = DoctorProfile.objects.filter(county=region_id)
    # all_doctors = DoctorProfile.objects.get(county=region_id)
    # user_list = all_doctors.doctor_profiles.all()
    context = {'doctor_list': doctor_list}
    return render(request, 'healthcare/view_doctors.html', context=context)
