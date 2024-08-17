from django import forms
from .models import StudentApplication,ParcelApplication

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ['user_name', 'user_email', 'message', 'user_contact_number']

class ParcelApplicationForm(forms.ModelForm):
    class Meta:
        model = ParcelApplication
        fields = ['user_name', 'user_email', 'message', 'user_contact_number']
