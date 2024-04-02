"""
URL configuration for webAppProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospAuth.views import PatientLogin,PatientSignUp
from hospPatient.views import PatientDashboard,PatienteditMyProfile,BookAppointment,PatientAppointments,mySession
from hospAdmin.views import AdminLogin,AdminDashboard,createDoctor,AllDoctors,editDoctor,AllPatients,editPatient,createPatient,allAppointments,assignAppointment,AdminviewPatientSession
from hospDoctor.views import DoctorDashboard,DoctorLogin,myAppointments,beginSession,viewPatientSession,doctoreditMyProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patientSignUp/',PatientSignUp, name="PatientSignUp"),
    path('createDoctor/<int:admin_id>/',createDoctor, name="createDoctor"),
    path('AdminDashboard/<int:admin_id>/',AdminDashboard, name="AdminDashboard"),
    path('createPatient/<int:admin_id>/',createPatient, name="createPatient"),
    path('editDoctor/<int:admin_id>/<int:user_id>/',editDoctor, name="editDoctor"),
    path('editPatient/<int:admin_id>/<int:user_id>/',editPatient, name="editPatient"),
    path('editPatient/<int:admin_id>/<int:user_id>/',editPatient, name="editPatient"),
    path('PatienteditMyProfile/<int:user_id>/',PatienteditMyProfile, name="PatienteditMyProfile"),
    path('doctoreditMyProfile/<int:user_id>/',doctoreditMyProfile, name="doctoreditMyProfile"),
    path('BookAppointment/<int:user_id>/',BookAppointment, name="BookAppointment"),
    path('patientDashboard/<int:user_id>/',PatientDashboard, name="patientDashboard"),
    path('DoctorDashboard/<int:user_id>/',DoctorDashboard, name="DoctorDashboard"),
    path('myAppointments/<int:user_id>/',myAppointments, name="myAppointments"),
    path('viewPatientSession/<int:user_id>/<int:appointment_id>/',viewPatientSession, name="viewPatientSession"),
    path('AdminviewPatientSession/<int:admin_id>/<int:appointment_id>/',AdminviewPatientSession, name="AdminviewPatientSession"),
    path('DoctorLogin/',DoctorLogin, name="DoctorLogin"),
    path('AllDoctors/<int:admin_id>/',AllDoctors, name="AllDoctors"),
    path('allAppointments/<int:admin_id>/',allAppointments, name="allAppointments"),
    path('PatientAppointments/<int:user_id>/',PatientAppointments, name="PatientAppointments"),
    path('assignAppointment/<int:admin_id>/<int:appointment_id>/',assignAppointment, name="assignAppointment"),
    path('beginSession/<int:user_id>/<int:appointment_id>/',beginSession, name="beginSession"),
    path('mySession/<int:user_id>/<int:appointment_id>/',mySession, name="mySession"),
    path('AllPatients/<int:admin_id>/',AllPatients, name="AllPatients"),
    path('adminLogin/',AdminLogin, name="AdminLogin"),
    path('',PatientLogin, name="PatientLogin"),
    path('',PatientLogin, name="PatientLogin"),
]
