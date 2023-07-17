from doctor.api.serializers import DoctorSerializer, DepartmentSerializer
from rest_framework import generics
from doctor.models import Doctor,Departments
from rest_framework.permissions import IsAuthenticated


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[IsAuthenticated]

class OneDoctor(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes=[IsAuthenticated]
    
    
class DepartmentList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes=[IsAuthenticated]

class OneDepartment(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes=[IsAuthenticated]