from django.shortcuts import render,redirect
from doctor.models import Doctor, Departments
from appointment.models import Appointment
from patient.models import Patient

from datetime import date



def appointment(request):
    departments= Departments.objects.all()
    doctors = Doctor.objects.all()
    context={
        'departments':departments,
        'doctors':doctors
    }
    
    if request.method == 'POST':
        patient_id= request.POST.get('patient_id')
        department_id= request.POST.get('department_id')
        doctor_id= request.POST.get('doctor_id')
        appointment_date= request.POST.get('date')
        
        patient_name=Patient.objects.get(id=patient_id)
        department_name=Departments.objects.get(id=department_id)
        doctor_name=Doctor.objects.get(id=doctor_id)
        
        Appointment.objects.create(patient_name=patient_name, department_name=department_name,doctor_name=doctor_name,appoinment_date=appointment_date).save()
        return redirect('appointment_list')  
    return render(request,'patient_dashboard/appointment.html',context)

def all_appointments(request):
    today = date.today()
    
    user=request.user.id
    
    appointments=Appointment.objects.filter(patient_name_id=user).order_by('-appoinment_date')
    context={
        'appointments': appointments,
        'today':today,
    }
    return render(request,'patient_dashboard/all_appointments.html',context)

