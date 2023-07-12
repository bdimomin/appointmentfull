from django.urls import path
from patient.api.views import get_patients,patient_details, login_view

urlpatterns = [
    path('<int:pk>/',patient_details, name="patient_details"),
    path('list/',get_patients, name="patient_list"),
    path('login/',login_view, name="login_view"),
    
]
