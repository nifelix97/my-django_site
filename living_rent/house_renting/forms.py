from django import forms
from .models import StudentApplication,ParcelApplication,CarApplication,Apartment

class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = ['user_name', 'user_email', 'message', 'user_contact_number']

class ParcelApplicationForm(forms.ModelForm):
    class Meta:
        model = ParcelApplication
        fields = ['user_name', 'user_email', 'message', 'user_contact_number']

class CarApplicationForm(forms.ModelForm):
    class Meta:
        model = CarApplication
        fields = ['user_name', 'user_email', 'message', 'user_contact_number']

class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['landlord', 'address', 'type', 'available', 'rent', 'description', 'main_image', 'video']
