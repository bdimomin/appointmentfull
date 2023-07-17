from django.urls import path
from doctor.api.views import DoctorList,OneDoctor,DepartmentList,OneDepartment

urlpatterns = [
    path('doctor/list/',DoctorList.as_view(),name='doctor_list'),
    path('doctor/<int:pk>/',OneDoctor.as_view(),name='one_doctor'),
    path('department/list/',DepartmentList.as_view(),name='doctor_list'),
    path('department/<int:pk>/',OneDepartment.as_view(),name='one_department'),
]
