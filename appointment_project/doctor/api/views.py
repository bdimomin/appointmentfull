from doctor.api.serializers import DoctorSerializer, DepartmentSerializer
from rest_framework import generics
from doctor.models import Doctor,Departments


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class OneDoctor(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    
    
class DepartmentList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer

class OneDepartment(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer