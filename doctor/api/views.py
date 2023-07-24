from doctor.api.serializers import DoctorSerializer, DepartmentSerializer
from rest_framework import generics
from doctor.models import Doctor,Departments
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from doctor.models import Doctor, Departments


class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes=[IsAuthenticated]

class OneDoctor(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # permission_classes=[IsAuthenticated]
    
    
class DepartmentList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes=[IsAuthenticated]

class OneDepartment(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes=[IsAuthenticated]

@api_view(['POST'])
def login_view(request):
    email= request.data['email']
    password= request.data['password']
    
    user = Doctor.objects.filter(email=email).first()
    
    if user is None:
        raise AuthenticationFailed("User not found")
    
    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect password")
    
    return Response({
        'message':'Successfully logged_in'
    })