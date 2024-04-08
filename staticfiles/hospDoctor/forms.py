from django import forms

class DoctorForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    specialty = forms.CharField(max_length=255)
