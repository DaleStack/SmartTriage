from django.urls import path
from .views import triage_view

urlpatterns = [
    path('patients/', triage_view, name='triage'),
]
