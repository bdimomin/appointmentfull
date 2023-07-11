from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse

from patient.api.serializers import PatientSerializer,PatientAddSerializer
from patient.models import Patient
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['GET','POST'])
def get_patients(request):
    if request.method == 'GET':
        patients= Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PatientAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    
@api_view(['GET'])
def patient_details(request,pk):
    try:
        patient= Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response({'message':'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
@api_view(['POST'])
def login_view(request):
    email= request.data['email']
    password= request.data['password']
    
    user = Patient.objects.filter(email=email).first()
    
    if user is None:
        raise AuthenticationFailed("User not found")
    
    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect password")
    
    return Response({
        'message':'Successfully logged_in'
    })