from django import forms

class AppointmentForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    purpose = forms.CharField(max_length=100)
    