from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from hospPatient.forms import PatientForm
from hospPatient.models import Patient
from hospAuth.models import Hospuser
from hospDoctor.models import Doctor
from datetime import datetime
from hospPatient.models import Patient
from hospAdmin.models import Session,Appointment
from hospAdmin.forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

date_format = '%m/%d/%Y %I:%M %p'

# Create your views here.
@login_required
def PatientDashboard(request,user_id):
    message_dict = {
        # 'success': False,
        # 'error': False
    }
    counts = {
        'sessions_count':0,
        'pending_appointment_count':0,
        'comp_appointment_count':0,
        'appointment_count':0,
        'patients_count':0

    }
    user = Hospuser.objects.get(id=user_id)
    
    patient = Patient.objects.get(user=user)

    user_data={
        'type':'patient',
        'data':user
    }
    if Session.objects.filter(patient=patient).exists():
        sessions_count = Session.objects.filter(patient=patient).count()
        counts['sessions_count'] = sessions_count
    
    if Appointment.objects.filter(patient=patient).exists():
        pending_appointment_count = Appointment.objects.filter(patient=patient,status="PENDING").count()
        counts['pending_appointment_count'] = pending_appointment_count
  
    if Appointment.objects.filter(patient=patient).exists():
        comp_appointment_count = Appointment.objects.filter(patient=patient,status="COMPLETED").count()
        counts['comp_appointment_count'] = comp_appointment_count
    
  
    if Appointment.objects.filter(patient=patient).exists():
        appointment_count = Appointment.objects.filter(patient=patient,status="PENDING").count()
        counts['appointment_count'] = appointment_count
    
  
    return render(request, 'patientDashboard.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'counts':counts,'patient':patient})

@csrf_exempt 
def PatienteditMyProfile(request,user_id):
    message_dict = {
        'success': None,
        'error': None
    }
    user = Hospuser.objects.get(id=user_id)
    user_data={
        'type':'patient',
        'data':user,
    }  
    
    
    if Patient.objects.filter(user=user).exists():
        patient = Patient.objects.get(user=user)
        return render(request, 'PatienteditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'patient':patient}) # Replace 'success-page' with your desired URL
        
    
    
   
    if request.method == 'POST' :
            
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        
        try:
            dob =datetime.strptime(date_of_birth,date_format)
        except:
            date_object = datetime.strptime(date_of_birth, '%b. %d, %Y')
            date_object1 = datetime.strptime(date_object.strftime('%m/%d/%Y'), '%m/%d/%Y')
            dob = date_object1.strftime('%Y-%m-%d')
        
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.password=password
        
        patient.gender=gender
        patient.date_of_birth=dob
        
        user.save()
        patient.save()
    
        message_dict["success"] = 'Your Profile Updated'
        patient = Patient.objects.get(user=user)
    
        return render(request, 'PatienteditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'patient':patient}) # Replace 'success-page' with your desired URL
        
    return render(request, 'PatienteditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'patient':patient})


@csrf_exempt 
def BookAppointment(request,user_id):

    message_dict = {
        # 'success': False,
        # 'error': False
    }
    doctors = Doctor.objects.all()
    user = Hospuser.objects.get(id=user_id)
    patient = Patient.objects.get(user=user)
    
    user_data={
        'type':'patient',
        'data':user
    }
    
    if request.method == 'POST':
         
        if request.POST.get('doc_id') is not None:
            doc_id = request.POST.get('doc_id')
            
            print(doc_id,"sssssssssssss")
            
            dateAndTime = request.POST.get('date_and_time')
            purpose = request.POST.get('purpose')
            datetime_obj = datetime.strptime(dateAndTime, "%m/%d/%Y %I:%M %p")
            
            date_part = datetime_obj.date()  # Get the date part
            time_part = datetime_obj.time()

            doctor = Doctor.objects.get(id=doc_id)
            
            
            appointment = Appointment(patient=patient, doctor=doctor,purpose=purpose,
                                    date=date_part, time=time_part)
            appointment.save()
            message_dict["success"] = 'Appointment Booked Successfully'
            return render(request, 'bookAppointment.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'patient':patient}) 
        else:
            message_dict["error"] = 'Select Doctor'
            return render(request, 'bookAppointment.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'patient':patient,'doctors':doctors}) 
      
    return render(request, 'bookAppointment.html', context={'messages': message_dict,'user_data':user_data,'doctors': doctors,'user_id':user_id,'patient':patient})

@csrf_exempt
def PatientAppointments(request,user_id):
    message_dict = {
    }
    
    user = Hospuser.objects.get(id=user_id)
    patient = Patient.objects.get(user=user)
    
    appointments=[]
    
    if Appointment.objects.filter(patient=patient).exists:
        appointments = Appointment.objects.filter(patient=patient)
    
    
    user_data={
        'type':'admin',
        'data':user
    }
    
        
        

    return render(request, 'PatientAppointments.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id, "appointments":appointments})
#
@csrf_exempt
def mySession(request,user_id,appointment_id):
    message_dict = {
    }
    doctors = Doctor.objects.all()
 
    user = Hospuser.objects.get(id=user_id)
    appointment = Appointment.objects.get(id=appointment_id)
    
    if Session.objects.filter(appointment=appointment).exists:
            session = Session.objects.get(appointment=appointment)
            
    
    user_data={
        'type':'admin',
        'data':user
    }
    
    return render(request, 'mySession.html', context={'messages': message_dict,'user_data':user_data,'doctors': doctors,'user_id':user_id,'session':session,'user_id':user_id})   

