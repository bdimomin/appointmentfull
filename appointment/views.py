from django.shortcuts import render,redirect
from doctor.models import Doctor, Departments
from appointment.models import Appointment
from patient.models import Patient
from doctor.models import Doctor
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


from datetime import date


@login_required(login_url="/login/")
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
        patient_email=request.POST.get('patient_email')
        patient_gender= request.POST.get('patient_gender')
        department_id= request.POST.get('department_id')
        doctor_id= request.POST.get('doctor_id')
        appointment_date= request.POST.get('date')
        user_id=request.user.id
        
       
        
        department_name=Departments.objects.get(id=department_id)
        doctor_name=Doctor.objects.get(id=doctor_id)
        
        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor_name).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
             Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,department_name=department_name,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
             send_mail(
                "Appointment Details",
                "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  1.",
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,department_name=department_name,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
               "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  "+str(appointment),
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            
        return redirect('appointment_list')  
    return render(request,'patient_dashboard/appointment.html',context)

@login_required(login_url="/login/")
def appointment2(request,department,doctor):
    department = Departments.objects.get(id=department)
    doctor= Doctor.objects.get(id=doctor)
    context={
        'department': department,
        'doctor':doctor,
    }
    
    if request.method == 'POST':
        patient_name= request.POST.get('patient_name')
        patient_age= request.POST.get('patient_age')
        patient_email=request.POST.get('patient_email')
        patient_gender= request.POST.get('patient_gender')
        appointment_date= request.POST.get('date')
        
        department = request.POST.get('department_id')
        doctor= request.POST.get('doctor_id')
        
        department_name=Departments.objects.get(id=department)
        doctor_name=Doctor.objects.get(id=doctor)
        
        user_id=request.user.id
        
        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor_name).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
             Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,department_name=department_name,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
             send_mail(
                "Appointment Details",
                "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  1.",
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,patient_name=patient_name,patient_age=patient_age,patient_email=patient_email,patient_gender=patient_gender,department_name=department_name,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
               "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  "+str(appointment),
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            
        return redirect('appointment_list')
    
    return render(request,'patient_dashboard/appointment2.html',context)


def load_doctors(request):
    department_id=request.GET.get('department_id')
    doctors=Doctor.objects.filter(department_id=department_id, is_active=True)
    context={
        'doctors':doctors
    }
    return render(request,'patient_dashboard/doctors.html',context)

def all_appointments(request):
    today = date.today()
    
    user=request.user.id
    
    appointments=Appointment.objects.filter(user_id=user,is_cancelled=0).order_by('-id')
    context={
        'appointments': appointments,
        'today':today,
    }
    return render(request,'patient_dashboard/all_appointments.html',context)



    
def delete_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('appointment_list')




def doctor_details(request):
    doctor_id=request.GET.get('doctor_id')
    doctor=Doctor.objects.filter(id=doctor_id)
    context={
        'doctor':doctor
    }
    return render(request,'patient_dashboard/doctor_details.html',context)



def cancel_appointment(request,pk):
    appointment=Appointment.objects.get(id=pk)
    
    if request.method == 'POST':
        
        cancel = request.POST.get("appointment_status")
        appointment=Appointment.objects.get(id=pk)
        appointment.is_cancelled = 1
        appointment.save()
        send_mail(
        "Appointment Details",
        "Your appointment has been cancelled",
        "appointmentdoctor1@gmail.com",
        [appointment.patient_email],
        fail_silently=False,
        )
        return redirect('appointment_list')
        
        
        
    return render(request, 'patient_dashboard/cancel_appointment.html', {"appointment": appointment})
    


