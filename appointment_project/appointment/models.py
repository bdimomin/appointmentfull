from django.db import models
from patient.models import Patient
from doctor.models import Doctor,Departments

# Create your models here.
class Appointment(models.Model):
    patient_name = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="patient_names", verbose_name="Patient Name")
    department_name = models.ForeignKey(Departments, on_delete=models.CASCADE,related_name="department_names",verbose_name="Department Name")
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name="doctor_names",verbose_name="Doctor Name")
    appoinment_date = models.DateField(verbose_name='Appoinment Date', null=True)

    
    class Meta:
        db_table = "appoinment"
        
    def __str__(self):
        return str(self.appoinment_date)
    


