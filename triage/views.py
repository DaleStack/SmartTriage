from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def triage_view(request):
    return render(request, 'triage/triage.html')
