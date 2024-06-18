from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from hospAuth.models import *
from hospDoctor.models import *
from hospAdmin.models import *
from datetime import datetime
from django.contrib import messages
date_format = '%m/%d/%Y %I:%M %p'

# Create your views here.
@csrf_exempt
def DoctorLogin(request):
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
                    return redirect(DoctorDashboard, user_id=user.id)
            else :
                message_dict["error"] = 'Invalid Doctor Credentials'
                return render(request, 'doctorLogin.html', {'messages': message_dict})
              
        except Doctor.DoesNotExist:
            pass
            message_dict["error"] = 'Invalid Doctor Credentials'
            return render(request, 'doctorLogin.html', {'messages': message_dict})
            
    return render(request, 'doctorLogin.html', {'messages': message_dict})

@csrf_exempt
def DoctorDashboard(request,user_id):
    message_dict = {
        # 'success': False,
        # 'error': False
    }
    counts = {
        'sessions_count':0,
        'appointment_count':0
    }
    user = Hospuser.objects.get(id=user_id)
    
    doctor = Doctor.objects.get(user=user)

    user_data={
        'type':'doctor',
        'data':doctor
    }
    if Session.objects.filter(doctor=doctor).exists():
        print(2)
        sessions_count = Session.objects.filter(doctor=doctor).count()
        counts['sessions_count'] = sessions_count
    
    if Appointment.objects.filter(doctor=doctor).exists():
        print(3)
        
        appointment_count = Appointment.objects.filter(doctor=doctor).count()
        counts['appointment_count'] = appointment_count
    
  
    
    return render(request, 'doctorDashboard.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'counts':counts,'doctor':doctor})

@csrf_exempt
def myAppointments(request,user_id):
    message_dict = {
    }
    
    user = Hospuser.objects.get(id=user_id)
    
    doctor = Doctor.objects.get(user=user)
    appointments=[]
    print(doctor)
    
    if Appointment.objects.filter(doctor=doctor).exists:
        appointments = Appointment.objects.filter(doctor=doctor)
    
    
    user_data={
        'type':'admin',
        'data':doctor
    }
    
        
        

    return render(request, 'myAppointments.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id, "appointments":appointments})

@csrf_exempt
def beginSession(request, user_id, appointment_id):
    message_dict = {}
    
    doctors = Doctor.objects.all()
    appointment = get_object_or_404(Appointment, id=appointment_id)
    user = get_object_or_404(Hospuser, id=appointment.doctor.user.id)
    doctor = get_object_or_404(Doctor, user=user)
    appointments = Appointment.objects.filter(doctor=doctor)

    user_data = {
        'type': 'patient',
        'data': doctor,
    }
    
    if request.method == 'POST':
        drugs_data = request.POST.getlist('drug_name')
        quantities = request.POST.getlist('quantity')

        if Session.objects.filter(appointment=appointment).exists():
            description = request.POST.get('description')

            for drug_name, quantity in zip(drugs_data, quantities):
                quantity = int(quantity)
                drug = get_object_or_404(Inventory, name=drug_name)
                
                if drug.quantity >= quantity:
                    drug.quantity -= quantity
                    drug.save()
                else:
                    messages.error(request, f'Not enough {drug.name} in stock. Only {drug.quantity} left.')

            appointment.status = "COMPLETED"
            appointment.save()
            session = Session.objects.create(
                patient=appointment.patient,
                appointment=appointment,
                doctor=appointment.doctor,
                description=description
            )
            session.save()
            messages.success(request, 'Appointment Updated Successfully')

            return redirect('myAppointments', user_id=user_id)

    drugs = Inventory.objects.all()
    
    return render(request, 'beginSession.html', {
        'messages': message_dict,
        'user_data': user_data,
        'doctors': doctors,
        'user_id': user_id,
        'appointment': appointment,
        'drugs': drugs
    })

@csrf_exempt
def viewPatientSession(request,user_id,appointment_id):
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
    
    return render(request, 'viewPatientSession.html', context={'messages': message_dict,'user_data':user_data,'doctors': doctors,'user_id':user_id,'session':session,'user_id':user_id})   


@csrf_exempt 
def doctoreditMyProfile(request,user_id):
    message_dict = {
        'success': None,
        'error': None
    }
    user = Hospuser.objects.get(id=user_id)
    doctor = Doctor.objects.get(user=user)
    
    user_data={
        'type':'doctor',
        'data':doctor,
    } 
    
    
    
        
    
  
   
    if request.method == 'POST' :
            
        if Doctor.objects.filter(user=user).exists():
            
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password = request.POST.get('password')
            specialty = request.POST.get('specialty')
            
            user.username=username
            user.first_name=first_name
            user.last_name=last_name
            user.password=password
            
            doctor.specialty=specialty
            
            user.save()
            doctor.save()
        
            message_dict["success"] = 'Your Profile Updated' # type: ignore
        
            return render(request, 'doctoreditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'doctor':doctor}) # Replace 'success-page' with your desired URL
        else:
            doctor = Doctor.objects.get(user=user)
            return render(request, 'DoctoreditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'doctor':doctor}) # Replace 'success-page' with your desired URL
        
    return render(request, 'doctoreditMyProfile.html', context={'messages': message_dict,'user_data':user_data,'user_id':user_id,'doctor':doctor})
