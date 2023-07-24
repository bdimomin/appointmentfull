from django.shortcuts import render
from doctor.models import Doctor, DoctorsProfile


def frontpage(request):
    doctors= Doctor.objects.all()
    return render(request, 'frontpage/index.html',{'doctors':doctors})

