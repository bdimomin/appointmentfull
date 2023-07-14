from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('patient/',include('patient.urls')),
    path('patient/appointment/',include('appointment.urls')),
    
    path('doctor/',include('doctor.urls')),
    
    
    path('api/patient/',include('patient.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('',include('django.contrib.auth.urls')),
]
