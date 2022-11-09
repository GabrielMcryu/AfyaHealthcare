from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from .models import UserProfile

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
            return render(request, 'healthcare/finish.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def finishView(request):
    return render(request, 'healthcare/finish.html')

def dashBoardView(request):
    return render(request, 'healthcare/dashboard.html')