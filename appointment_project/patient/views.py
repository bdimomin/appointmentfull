from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import PatientRegistrationForm,UserLoginForm


@login_required(login_url='patient/login/')
def home_view(request):
    return render(request,'dashboard.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 
    context={}
    if request.method=="POST":
        form=PatientRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
        context['register_form']=form
    else:
        form=PatientRegistrationForm()
        context['register_form']=form
    return render(request,'registration/sign_up.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard') 

    context={}
    if request.method=="POST":
        form= UserLoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('dashboard')
    else:
        form=UserLoginForm()
        context['login_form']=form
    return render(request,'registration/login.html',context)

def logout_view(request):
    logout(request)
    return redirect('login')
        