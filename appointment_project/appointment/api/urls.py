from django.urls import path
from appointment.api.views import *

urlpatterns = [
    path('new/',new_appointment,name='new_appointment'),
    path('list/<int:bmdc>/<str:date>/',Appointment_list.as_view(),name='appointment_list'),
]
