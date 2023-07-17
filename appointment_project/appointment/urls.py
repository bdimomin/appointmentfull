from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointment,name="appointment"),
    path('list/',views.all_appointments,name='appointment_list'),
    path('applist/',views.date_doc_appointment,name="date_doc_appointment"),
    
    path('load-doctor/', views.load_doctors, name='ajax_load_doctors'),
    
]
