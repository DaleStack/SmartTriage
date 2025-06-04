from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class DoctorModel(AbstractUser):
    def __str__(self):
        return f"Dr. {self.last_name}"
