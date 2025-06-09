from django.urls import path
from .views import triage_view, triage_form

urlpatterns = [
    path('triage/', triage_view, name='triage'),
    path('triage/forms/', triage_form, name='triage-form'),


]
