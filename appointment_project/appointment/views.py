from django.shortcuts import render,redirect
from doctor.models import Doctor, Departments
from appointment.models import Appointment
from patient.models import Patient
from doctor.models import Doctor
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


from datetime import date



def appointment(request):
    departments= Departments.objects.all()
    # doctors = Doctor.objects.all()
    context={
        'departments':departments,
        
    }
    
    if request.method == 'POST':
        # patient_id= request.POST.get('patient_id')
        patient_name= request.POST.get('patient_name')
        patient_age= request.POST.get('patient_age')
        patient_gender= request.POST.get('patient_gender')
        patient_email = request.POST.get('patient_email')
        department_id= request.POST.get('department_id')
        doctor_id= request.POST.get('doctor_id')
        appointment_date= request.POST.get('date')
        user_id=request.user.id
        
       
        
        department_name=Departments.objects.get(id=department_id)
        doctor_name=Doctor.objects.get(id=doctor_id)
        
        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor_name).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
             Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_gender=patient_gender,patient_email=patient_email,department_name=department_name,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_gender=patient_gender,patient_email=patient_email,department_name=department_name,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            def success(request,uid):
                template = render_to_string('email.html', {'name': request.user.profile.name})
                email = EmailMessage (
                    'Your Appointment is Confirmed',
                    template,
                    settings.EMAIL_HOST_USER,
                    [request.user.profile.email],
                )

        return redirect('appointment_list')  
    return render(request,'patient_dashboard/appointment.html',context)


def load_doctors(request):
    department_id=request.GET.get('department_id')
    doctors=Doctor.objects.filter(department_id=department_id)
    context={
        'doctors':doctors
    }
    return render(request,'patient_dashboard/doctors.html',context)

def all_appointments(request):
    today = date.today()
    
    user=request.user.id
    
    appointments=Appointment.objects.filter(user_id=user).order_by('-appoinment_date')
    context={
        'appointments': appointments,
        'today':today,
    }
    return render(request,'patient_dashboard/all_appointments.html',context)


@login_required(login_url='patient/login/')
def date_doc_appointment(request):
    
    if request.user.is_superuser:
        doctors=Doctor.objects.all()
        context={}
    
        if request.method == 'POST':
            doc_name= request.POST.get('doctor_id')
            date= request.POST.get('date')
            
            appointments=Appointment.objects.filter(doctor_name_id=doc_name, appoinment_date=date).order_by('serial_number')
            
            context={
                'appointments':appointments,
                'doctors':doctors,
            }
            return render(request,'patient_dashboard/datedocwiseapp.html',context)
        
        return render(request,'patient_dashboard/datedocwiseapp.html',{'doctors':doctors})
    else:
       
        return redirect('dashboard')
    
    
def delete_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('appointment_list')
    


