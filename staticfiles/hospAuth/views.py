from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from hospPatient.forms import PatientForm
from hospPatient.models import Patient
from hospAuth.models import Hospuser
from datetime import datetime
from hospPatient.models import Patient
from hospAuth.models import Hospuser
from hospAdmin.models import Session,Appointment
from hospPatient.views import PatientDashboard

date_format = '%m/%d/%Y %I:%M %p'

# Create your views here.
@csrf_exempt
def PatientLogin(request):
    message_dict = {
        # 'success': False,
        # 'error': False
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            if   Hospuser.objects.filter(username=username,password=password).exists():
            
                user = Hospuser.objects.get(username=username,password=password)
                
                if user:
                    return redirect(PatientDashboard, user_id=user.id)
            else :
                message_dict["error"] = 'Invalid Patient Credentials'
                return render(request, 'patientLogin.html', {'messages': message_dict})
              
        except Patient.DoesNotExist:
            pass
            message_dict["error"] = 'Invalid Patient Credentials'
            return render(request, 'patientLogin.html', {'messages': message_dict})
            
    return render(request, 'patientLogin.html', {'messages': message_dict})

@csrf_exempt    
def PatientSignUp(request):
    message_dict = {
        'success': None,
        'error': None
    }
   
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            first_name = data['first_name']
            username = data['username']
            last_name = data['last_name']
            password = data['password']
            gender = data['gender']
            date_of_birth = data['date_of_birth']

            # Create a new Hospuser instance
            if Hospuser.objects.filter(username=username).exists():
                message_dict["error"] = 'User name is in use'
                return render(request, 'patientSignUp.html', context={'messages': message_dict}) # Replace 'success-page' with your desired URL

            else: 
                dob =datetime.strptime(date_of_birth,date_format)
                user = Hospuser.objects.create(
                    first_name=first_name,
                    username=username,
                    last_name=last_name,
                    password=password
                )
              
                
                
                patient = Patient.objects.create(
                    user=user,
                    gender=gender,
                    date_of_birth=dob
                )

                message_dict["success"] = 'Patient Profile Created'
                return render(request, 'patientSignUp.html', context={'messages': message_dict}) # Replace 'success-page' with your desired URL

        else:
            message_dict["error"] = 'Invalid Patient Credentials'
            return render(request, 'patientSignUp.html', context={'messages': message_dict})
    else:
        form = PatientForm()

    return render(request, 'patientSignUp.html', context={'messages': message_dict})


