from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctor.forms import DoctorRegistrationForm,DoctorLoginForm,DoctorProfileUpdate, DoctorProfileDetails
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from doctor.models import Doctor, DoctorsProfile, Departments
from appointment.models import Appointment
from datetime import date


@login_required(login_url='doctor/login/')
def doctor_home(request):
    return render(request,'doctor/dashboard.html')

def doctor_reg(request):
    form = DoctorRegistrationForm()
    if request.method =='POST':
        form = DoctorRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Congratulations Sir, You have successfully registered. Please Wait for the internal Verification.")
        else:
            return HttpResponse("Something Wrong Sir, Please try again")
        
    return render(request,'doctor/registration.html',{'form':form})


def doctor_login(request):
    form = DoctorLoginForm()
    if request.method == 'POST':
        
        form = DoctorLoginForm(request.POST)
        
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            doctor=authenticate(request,email=email,password=password)
            if doctor is not None:
                login(request,doctor)
                return redirect('doctor_home')
                
            else:
               
                form=DoctorLoginForm()
                return render(request,'registration/login.html',{'form':form})
            
    return render(request,'doctor/login.html',{'form':form})

def doctor_profile_update(request,pk):
    doctor= Doctor.objects.get(pk=pk)
    form =DoctorProfileUpdate(instance=doctor)
    if request.method == 'POST':
        form=DoctorProfileUpdate(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_home')
    return render(request,'doctor/edit_doctor.html',{'form':form})


def appointment_list_view(request,pk):
    if request.method=='POST':
        pk = request.user.id
        date = request.POST.get('date')
        appointments = Appointment.objects.filter(doctor_name_id = pk, appoinment_date = date)
        return render(request,'doctor/appointment_list.html', {'appointments': appointments})
    else:
        return render(request,'doctor/appointment_list.html')
    


def doctor_logout(request):
    logout(request)
    return redirect('frontpage')

def profile_doc(request,pk):
    doctor= Doctor.objects.get(pk=pk)
    department= Departments.objects.get(id=doctor.department_id)
    details = DoctorsProfile.objects.filter(doctor_id=pk)
    context={
        'doctor':doctor,
        'details':details,
        'department':department
    }
    return render(request,'doctor/profile.html',context)

def doctor_profile_details(request):
    if request.method =='POST':
        form = DoctorProfileDetails(request.POST)
        form.instance.doctor_id = request.user
        if form.is_valid():
            form.save()
            return redirect('doctor_home')
    else:
        form = DoctorProfileDetails()
    return render(request, 'doctor/doctor_profile_details.html',{'form':form})
