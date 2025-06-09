from django import forms
from .models import TriageModel

class TriageModelForm(forms.ModelForm):
    class Meta:
        model = TriageModel
        exclude = ['assigned_doctor', 'submitted_at', 'reviewed', 'ai_soap']