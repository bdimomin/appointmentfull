from rest_framework.response import Response
from appointment.api.serializers import AppointmentSerializer
from appointment.models import Appointment
from doctor.models import Doctor

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics





def new_appointment(request):
    pass 

class Appointment_list(generics.ListAPIView):
    serializer_class=AppointmentSerializer
    def get_queryset(self):
        bmdc=self.kwargs['bmdc']
        doc= Doctor.objects.get(bmdc_registration_number=bmdc)
        doc_id = doc.id
        date=self.kwargs['date']
        return Appointment.objects.filter(doctor_name=doc_id,appoinment_date=date)