from django.shortcuts import render,redirect
from doctor.models import Doctor, Departments
from appointment.models import Appointment
from patient.models import Patient
from doctor.models import Doctor
from django.db.models import Max
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from twilio.rest import Client


from datetime import date, timedelta, datetime
from django.utils import timezone
from .models import Appointment
# from .utils import send_sms

from django.conf import settings
from twilio.rest import Client


def send_sms_reminder(patient_name, phone_number, appointment_datetime,reminder_time, doctor_name):
    # Your Twilio settings from Django settings
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = settings.TWILIO_PHONE_NUMBER

    client = Client(account_sid, auth_token)

    message = f"Hello {patient_name}, your appointment with Dr. {doctor_name} is scheduled at {appointment_datetime}. Don't forget!"

    try:
        current_time = timezone.now()
        print("Current Time:", current_time)
        print("Reminder Time:", reminder_time)
        if current_time >= reminder_time:
            message = client.messages.create(
                body=message,
                from_=twilio_phone_number,
                to=phone_number
            )
            print("Reminder SMS Sent!")
            return True
        else:
            print("Reminder SMS Not Sent Yet.")
            return False
    except Exception as e:
        print("Error sending SMS:",str(e))
        return False


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
        patient_email=request.POST.get('patient_email')
        phone_number=request.POST.get('phone_number')
        department_id= request.POST.get('department_id')
        doctor_id= request.POST.get('doctor_id')
        appointment_date_str= request.POST.get('date')
        appointment_time =request.POST.get('time')
        user_id=request.user.id
        
               
        department_name=Departments.objects.get(id=department_id)
        doctor_name=Doctor.objects.get(id=doctor_id)
        
        appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
        appointment_datetime = datetime.combine(appointment_date, datetime.strptime(appointment_time, '%H:%M').time())

        reminder_time = appointment_datetime - timedelta(hours=3)

        appointment=Appointment.objects.filter(appoinment_date=appointment_date, doctor_name=doctor_name).aggregate(Max('serial_number'))['serial_number__max']
        
        if not appointment:
            
            Appointment.objects.create(user_id=user_id,appointment_time=appointment_time,patient_name=patient_name,patient_age=patient_age,patient_gender=patient_gender,patient_email=patient_email,phone_number=phone_number,department_name=department_name,doctor_name=doctor_name,serial_number=1,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
                "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  1.",
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            # print(message.sid)
            # appointment_datetime = datetime.combine(appointment_date, appointment_time)
            send_sms_reminder(patient_name, phone_number, appointment_datetime, reminder_time,doctor_name)    

           
        else:
            appointment+=1
            Appointment.objects.create(user_id=user_id,appointment_time=appointment_time,patient_name=patient_name,patient_age=patient_age,patient_gender=patient_gender,patient_email=patient_email,phone_number=phone_number,department_name=department_name,doctor_name=doctor_name,serial_number=appointment,appoinment_date=appointment_date).save()
            send_mail(
                "Appointment Details",
               "Congratulations Mr/Mrs. "+ patient_name +", You have taken a serial on "+str(appointment_date)+" of doctor Mr." +str(doctor_name)+ ". Your Serial number is :  "+str(appointment),
                "appointmentdoctor1@gmail.com",
                [patient_email],
                fail_silently=False,
            )
            # appointment_datetime = datetime.combine(appointment_date, appointment_time)
            send_sms_reminder(patient_name, phone_number, appointment_datetime, reminder_time, doctor_name)    
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
    
    # send_sms_reminder(patient_name, patient_phone_number, appointment_date, doctor_name)
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
    


