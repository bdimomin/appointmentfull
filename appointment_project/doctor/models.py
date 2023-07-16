from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Departments(models.Model):
    department_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "departments"
    
    def __str__(self):
        return self.department_name

class DoctorManager(BaseUserManager):
    def create_user(self,email,name,phone,department,bmdc_registration_number,password=None):
        if not email:
            raise ValueError("Email is required")
        if not phone:
            raise ValueError("Phone is required")
        if not name:
            raise ValueError("Name is required")
        if not department:
            raise ValueError("Department is required")
        
        if not bmdc_registration_number:
            raise ValueError("BM&DC Registration Number is required")
        
        user =self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            department=department,
            bmdc_registration_number=bmdc_registration_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # def create_superuser(self,email,name,phone,department,bmdc_registration_number,password=None):
    #     user=self.create_user(
    #         email=self.normalize_email(email),
    #         name=name,
    #         phone=phone,
    #         department=department,
    #         bmdc_registration_number=bmdc_registration_number,
    #         password=password
    #     )
    #     user.is_admin=True
    #     user.is_superuser=True
    #     user.is_staff=True
    #     user.save(using=self._db)
    #     return user
        

class Doctor(AbstractBaseUser):
    email = models.EmailField(max_length=100, verbose_name="Email Address",unique=True)
    name = models.CharField(max_length=100, verbose_name="Name")
    phone=models.CharField(max_length=20, verbose_name="Phone", unique=True)
    department=models.ForeignKey(Departments,verbose_name="Department", on_delete=models.CASCADE, related_name='department')
    bmdc_registration_number=models.CharField(max_length=50,verbose_name="BM&DC Registration Number",unique=True)
    
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['name','phone','department','bmdc_registration_number']
    
    objects=DoctorManager()
    
    def __str__(self):
        return self.name 

    def has_perm(self, perm,obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    