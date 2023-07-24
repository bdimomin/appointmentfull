from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment,name="appointment"),
    path('list/',views.all_appointments,name='appointment_list'),
    path('delete/<int:pk>/',views.delete_appointment,name='delete_appointment'),
    
    path('load-doctor/', views.load_doctors, name='ajax_load_doctors'),
    path('doctor-details/', views.doctor_details, name='ajax_doctor_details'),
    
    path('cancel/<int:pk>/', views.cancel_appointment,name ='cancel_appointment'),
    
]
