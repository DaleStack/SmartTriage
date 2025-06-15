from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TriageModelForm
from .models import TriageModel
from django.contrib import messages
import google.generativeai as genai
from django.conf import settings
import markdown
from django.utils.safestring import mark_safe

# Create your views here.

# HOME VIEW
@login_required
def triage_view(request):
    return render(request, 'triage/home/triage.html')

genai.configure(api_key=settings.GEMINI_API_KEY)

#GEMINI API RESPONSE
def generate_soap_note(data):
    prompt = f"""
    Generate a medical SOAP note based on the following information:

    Full Name: {data.get('full_name')}
    Age: {data.get('age')}
    Gender: {data.get('gender')}
    Phone Number: {data.get('phone_number')}

    Symptoms: {data.get('symptoms')}
    Duration: {data.get('duration')}
    Pain Level: {data.get('pain_level')}

    Existing Conditions: {data.get('existing_conditions')}
    Allergies: {data.get('allergies')}
    Current Medications: {data.get('current_medications')}
    Recent Surgery: {"Yes" if data.get('surgery') else "No"} in the past 30 days

    Format the response as a SOAP (Subjective, Objective, Assessment, Plan) note.
    Return the SOAP only, nothing else. Don't add any other sentences, just concise SOAP report.
    Do not add bullet points. Keep the formatting consistent. For the "S" in SOAP, do not put the informartion in one line. Break it and add bold for every category.
    """

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)

    html_output = markdown.markdown(response.text.strip())
    return mark_safe(html_output)


# FORMS VIEW
@login_required
def triage_form(request):
    if request.method == 'POST':
        form = TriageModelForm(request.POST)
        if form.is_valid():
            triage = form.save(commit=False)
            triage.assigned_doctor = request.user

            # Prepare data to pass to Gemini
            form_data = form.cleaned_data

            # Generate AI SOAP note
            try:
                ai_note = generate_soap_note(form_data)
                triage.ai_soap = ai_note
            except Exception as e:
                messages.error(request, f"AI generation failed: {e}")
                triage.ai_soap = "AI note could not be generated."

            triage.save()
            messages.success(request, 'Form sent successfully!')
            return redirect('triage')
    else:
        form = TriageModelForm()

    return render(request, 'triage/forms/forms.html', {'form': form})

