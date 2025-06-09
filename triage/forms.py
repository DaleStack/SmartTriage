from django import forms
from .models import TriageModel

class TriageStep1Form(forms.ModelForm):
    class Meta:
        model = TriageModel
        fields = ['full_name', 'age', 'gender', 'phone_number']

class TriageStep2Form(forms.ModelForm):
    class Meta:
        model = TriageModel
        fields = ['symptoms', 'duration', 'pain_level']

class TriageStep3Form(forms.ModelForm):
    class Meta:
        model = TriageModel
        fields = ['existing_conditions', 'allergies', 'current medications', 'surgery']