from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import DoctorRegister, DoctorLogin

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
    return render(request, 'doctor/register.html', {'form': form})


# Doctor login view
def login_view(request):
    if request.method == 'POST':
        form = DoctorLogin(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            messages.success(request, f"Welcome back Dr. {user.username}!")
            return redirect('dashboard') 
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = DoctorLogin()
    return render(request, 'doctor/login.html', {'form': form})


# Doctor logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  
