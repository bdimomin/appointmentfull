from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment,name="appointment"),
    path('list/',views.all_appointments,name='appointment_list')
]
