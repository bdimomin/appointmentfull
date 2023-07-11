from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.hashers import make_password

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id','name','email','phone']
        
class PatientAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(PatientAddSerializer, self).create(validated_data)


    