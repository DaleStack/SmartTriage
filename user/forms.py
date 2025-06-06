from django import forms  
from .models import DoctorModel
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


# Registration form
class DoctorRegister(UserCreationForm):
    class Meta:
        model = DoctorModel
        fields = ['username', 'email']



class DoctorLogin(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(
            username=cleaned_data.get("username"),
            password=cleaned_data.get("password")
        )
        if not user:
            raise forms.ValidationError("Invalid username or password.")
        cleaned_data['user'] = user
        return cleaned_data

