# Generated by Django 4.2.3 on 2023-07-13 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_date', models.DateField(null=True, verbose_name='Appoinment Date')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_names', to='doctor.departments', verbose_name='Department Name')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_names', to='doctor.doctor', verbose_name='Doctor Name')),
                ('patient_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_names', to=settings.AUTH_USER_MODEL, verbose_name='Patient Name')),
            ],
            options={
                'db_table': 'appoinment',
            },
        ),
    ]
