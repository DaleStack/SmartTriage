from django.urls import path
from .views import triage_view

urlpatterns = [
    path('triage/', triage_view, name='triage'),
]
