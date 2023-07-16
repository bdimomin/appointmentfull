from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


from django.contrib import admin
from django.urls import path,include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
     path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
     
      path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
      
    path('',include('frontpage.urls')),
    
    
    path('admin/', admin.site.urls),
    
    path('patient/',include('patient.urls')),
    path('patient/appointment/',include('appointment.urls')),
    
    path('doctor/',include('doctor.urls')),
    path('api/',include('doctor.api.urls')),
    
    
    
    
    path('api/patient/',include('patient.api.urls')),
    
    path('api/appointment/',include('appointment.api.urls')),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('',include('django.contrib.auth.urls')),
]
