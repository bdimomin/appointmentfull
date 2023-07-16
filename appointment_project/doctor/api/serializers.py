from rest_framework import serializers
from doctor.models import Doctor, Departments

class DepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Departments
        fields='__all__'
    
class DoctorSerializer(serializers.ModelSerializer):
    
    department= serializers.StringRelatedField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True, format="%d-%m-%Y")
    
    class Meta:
        model = Doctor
        fields=['bmdc_registration_number','name','email','phone','department','date_joined']
        