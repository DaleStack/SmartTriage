from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import DoctorRegister, DoctorLogin
from triage.models import TriageModel
from django.contrib.auth.decorators import login_required

# AUTHENTICATION

# Doctor registration view
def register_view(request):
    if request.method == 'POST':
        form = DoctorRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login 
            messages.success(request, f"Welcome Dr. {user.username}!")
            return redirect('dashboard') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = DoctorRegister()
    return render(request, 'user/auth/register.html', {'form': form})


# Doctor login view
def login_view(request):
    if request.method == 'POST':
        form = DoctorLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, f"Welcome back Dr. {user.last_name}!")
            return redirect('dashboard') 
    else:
        form = DoctorLogin()
    return render(request, 'user/auth/login.html', {'form': form})


# Doctor logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  


# DASHBOARD VIEW

#Doctor Dashboard
@login_required
def dashboard_view(request):
    user = request.user

    triage_count = TriageModel.objects.filter(assigned_doctor=user).order_by("-submitted_at").count

        # Low Priority: 0–3
    low_priority_count = TriageModel.objects.filter(
        assigned_doctor=user,
        pain_level__gte=0,
        pain_level__lte=3
    ).count()

    # Medium Priority: 4–7
    med_priority_count = TriageModel.objects.filter(
        assigned_doctor=user,
        pain_level__gte=4,
        pain_level__lte=7
    ).count()

    # High Priority: 8–10
    high_priority_count = TriageModel.objects.filter(
        assigned_doctor=user,
        pain_level__gte=8,
        pain_level__lte=10
    ).count()

    patient_list = TriageModel.objects.filter(assigned_doctor=user).order_by("submitted_at")


    return render(request, 'user/dashboard/dashboard.html', {'user':user, 'triage_count':triage_count, "low_prio_count": low_priority_count, "med_prio_count": med_priority_count, "high_prio_count":high_priority_count, "patient_list":patient_list})


