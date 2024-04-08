from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from hospDoctor.forms import DoctorForm
from hospPatient.forms import PatientForm
from hospAdmin.models import Session,Appointment
from hospDoctor.models import Doctor
from hospPatient.models import Patient
from hospAuth.models import Hospuser
from .models import Admin
from datetime import datetime,date


date_format = '%m/%d/%Y %I:%M %p'

@csrf_exempt
def AdminLogin(request):
    message_dict = {
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            admin = Admin.objects.get(username=username,password=password)
            print(1)
            if admin:
                print(2)
                
                return redirect(AdminDashboard, admin_id=admin.id)
            else:
                print(2)
                return render(request, 'adminLogin.html', {'messages': message_dict})
        except Admin.DoesNotExist:
            pass
            message_dict["error"] = 'Invalid Admin Credentials'
            
    return render(request, 'adminLogin.html', {'messages': message_dict})

@csrf_exempt
def AdminDashboard(request,admin_id):
    message_dict = {
    }
    admin = Admin.objects.get(id=admin_id)
    user_data={
        'type':'admin',
        'data':admin
    }
    doctors_count = Doctor.objects.count()
    patients_count = Patient.objects.count()
    sessions_count = Session.objects.count()
    appointment_count = Appointment.objects.count()
    
    counts = {
        'doctors_count':doctors_count,
        'patients_count':patients_count,
        'sessions_count':sessions_count,
        'appointment_count':appointment_count
    }
    print(admin)
    return render(request, 'adminDashboard.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'counts':counts})

@csrf_exempt
def AllDoctors(request,admin_id):
    message_dict = {
    }
    admin = Admin.objects.get(id=admin_id)
    doctors = Doctor.objects.all()
    
    doctors_count = Patient.objects.count()
    
    counts = {
        'doctors_count':doctors_count
    }
    user_data={
        'type':'admin',
        'data':admin
    }
    if request.method == 'POST' and  request.POST.get('doctor_get') is not None:
        doctor_id = request.POST.get('doctor_get')
        
        doctor = Doctor.objects.get(id=doctor_id)
        
        user_data={
            'type':'admin',
            'data':admin
        }
        print(doctor_id)
        return render(request, 'editDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id, "doctor":doctor,'counts':counts})

    return render(request, 'allDoctors.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id, "doctors":doctors,'counts':counts})

@csrf_exempt
def allAppointments(request,admin_id):
    message_dict = {
    }
    admin = Admin.objects.get(id=admin_id)
    appointments = Appointment.objects.all()
    
    user_data={
        'type':'admin',
        'data':admin
    }
    
    appointment_count = Appointment.objects.count()
    
    counts = {
        'appointment_count':appointment_count
    }
        

    return render(request, 'allAppointments.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id, "appointments":appointments,'counts':counts})

@csrf_exempt
def AllPatients(request,admin_id):
    message_dict = {
    }
    admin = Admin.objects.get(id=admin_id)
    patients = Patient.objects.all()
    patients_count = Patient.objects.count()
    
    counts = {
        'patients_count':patients_count
    }
    user_data={
        'type':'admin',
        'data':admin
    }
    if request.method == 'POST' and  request.POST.get('patient_get') is not None:
        patient_id = request.POST.get('patient_get')
        
        patient = Patient.objects.get(id=patient_id)
        
        user_data={
            'type':'admin',
            'data':admin
        }
        
        return render(request, 'editPatient.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id, "patient":patient,'counts':counts})

    return render(request, 'AllPatients.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id, "patients":patients,'counts':counts})

@csrf_exempt
def createDoctor(request,admin_id):
    message_dict = {
        'success': None,
        'error': None
    }
    admin = Admin.objects.get(id=admin_id)
    user_data={
        'type':'admin',
        'data':admin
    }
    
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            first_name = data['first_name']
            username = data['username']
            last_name = data['last_name']
            password = data['password']
            specialty = data['specialty']

            if Hospuser.objects.filter(username=username).exists():
                message_dict["error"] = 'User name is in use'
                return render(request, 'createDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id}) # Replace 'success-page' with your desired URL

            else:
                user = Hospuser.objects.create(
                    first_name=first_name,
                    username=username,
                    last_name=last_name,
                    password=password
                )

                # Create a new Doctor instance associated with the Hospuser
                doctor = Doctor.objects.create(
                    user=user,
                    specialty=specialty
                )

                # Redirect to a success page or do further processing
                message_dict["success"] = 'Doctor Profile Created'
                return render(request, 'createDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id}) # Replace 'success-page' with your desired URL

        else:
            message_dict["error"] = 'Invalid Doctor Credentials'
            return render(request, 'createDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id})
    else:
        form = DoctorForm()

    return render(request, 'createDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id})

@csrf_exempt
def editDoctor(request,admin_id,user_id):
    message_dict = {
        'success': None,
        'error': None
    }
    admin = Admin.objects.get(id=admin_id)
    user = Hospuser.objects.get(id=user_id)
    user_data={
        'type':'admin',
        'data':admin
    } 
    doctor = Doctor.objects.get(user=user)

    if request.method == 'POST' and request.POST.get('delete') is not None :
        user.delete()
        doctors = Doctor.objects.all()
        
        return render(request, 'allDoctors.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'doctors':doctors})
   
    if request.method == 'POST' :
            
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        specialty = request.POST.get('specialty')
        print(specialty)
        
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.password=password
        doctor.specialty=specialty
        user.save()
        if user.save():
        # Create a new Hospuser instance
            message_dict["success"] = 'Doctor Profile Updated'
            doctor = Doctor.objects.get(user=user)
        
            return render(request, 'editDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'doctor':doctor}) # Replace 'success-page' with your desired URL
        else:
            return render(request, 'editDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'doctor':doctor})
        
    return render(request, 'editDoctor.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'doctor':doctor})
       
@csrf_exempt
def assignAppointment(request,admin_id,appointment_id):
    message_dict = {
        # 'success': False,
        # 'error': False
    }
    
    doctors = Doctor.objects.all()
    appointment = Appointment.objects.get(id=appointment_id)
    
    user_id = appointment.patient.user.id
    
    
    user_data={
        'type':'patient',
        'data':appointment,
    }
    
    if request.method == 'POST':
         
        if request.POST.get('doc_id') is not None:
            
            status = request.POST.get('status')
    

            appointment.status=status
            appointment.save()
            message_dict["success"] = 'Appointment Updated Successfully'
            return render(request, 'assignAppointment.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'appointment':appointment,'admin_id':admin_id,'doctors':doctors}) 
        else:
            message_dict["error"] = 'Select Doctor'
            return render(request, 'assignAppointment.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'appointment':appointment,'doctors':doctors,'admin_id':admin_id}) 
      
    return render(request, 'assignAppointment.html', context={'messages': message_dict,'user_data':user_data,'doctors': doctors,'user_id':user_id,'appointment':appointment,'admin_id':admin_id})   


@csrf_exempt 
def editPatient(request,admin_id,user_id):
    message_dict = {
        'success': None,
        'error': None
    }
    admin = Admin.objects.get(id=admin_id)
    user = Hospuser.objects.get(id=user_id)
    user_data={
        'type':'admin',
        'data':admin
    } 
    patient = Patient.objects.get(user=user)

    if request.method == 'POST' and request.POST.get('delete') is not None :
        user.delete()
        patients = Patient.objects.all()
        
        return render(request, 'allPatients.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'patients':patients})
   
    if request.method == 'POST' :
            
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        dob =datetime.strptime(date_of_birth,date_format)
        
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.password=password
        patient.gender=gender
        patient.date_of_birth=dob
        
        user.save()
        patient.save()
    
        message_dict["success"] = 'Patient Profile Updated'
        patient = Patient.objects.get(user=user)
    
        
    return render(request, 'editPatient.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id,'patient':patient})
        
@csrf_exempt
def createPatient(request,admin_id):
    message_dict = {
        'success': None,
        'error': None
    }
    admin = Admin.objects.get(id=admin_id)
    user_data={
        'type':'admin',
        'data':admin
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

            if Hospuser.objects.filter(username=username).exists():
                message_dict["error"] = 'User name is in use'

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

        else:
            message_dict["error"] = 'Invalid Patient Credentials'
            return render(request, 'createPatient.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id})
    else:
        form = PatientForm()

    return render(request, 'createPatient.html', context={'messages': message_dict,'user_data':user_data,'admin_id':admin_id})

@csrf_exempt
def AdminviewPatientSession(request,admin_id,appointment_id):
    message_dict = {
    }
    doctors = Doctor.objects.all()
 
    user = Hospuser.objects.get(id=admin_id)
    appointment = Appointment.objects.get(id=appointment_id)
    
    if Session.objects.filter(appointment=appointment).exists:
            session = Session.objects.get(appointment=appointment)
            
    
    user_data={
        'type':'admin',
        'data':user
    }
    
    return render(request, 'AdminviewPatientSession.html', context={'messages': message_dict,'user_data':user_data,'doctors': doctors,'admin_id':admin_id,'session':session})   
