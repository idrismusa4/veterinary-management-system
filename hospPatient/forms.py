from django import forms

class PatientForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    date_of_birth = forms.CharField(max_length=100)
