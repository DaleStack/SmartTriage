from django.db import models
from django.conf import settings

class TriageModel(models.Model):
    assigned_doctor = models.ForeignKey(settings.AUTH_USER_MODEL,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed = models.BooleanField(default=False)

    # Step 1: Personal Info
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,
                            choices=[('Male', 'Male'), 
                                     ('Female', 'Female'), 
                                     ('Other', 'Other')])
    phone_number = models.CharField(max_length=15)  

    # Step 2: Symptoms Assessment
    symptoms = models.TextField()
    duration = models.CharField(max_length=100)
    pain_level = models.IntegerField(
        choices=[(i, str(i)) for i in range(0, 11)] # 0 - 10 scale
    ) 

    # Step 3: Medical History
    existing_conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    current_medications = models.TextField(blank=True)
    surgery = models.BooleanField(default=False)  # If patient had surgery in the past 30 days

    # AI-generated SOAP note
    ai_soap = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Triage Note - {self.full_name} ({self.submitted_at})"
