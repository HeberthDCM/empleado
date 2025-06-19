from django.db import models
from applications.departamento.models import Departamento

# Create your models here. 
class Empleados(models.Model):
    job_choices = (
        ('0', 'Gerente'),
        ('1', 'Desarrollador'),
        ('2', 'Diseñador'),
        ('3', 'Analista'),
        ('4', 'Otro'),
    )


    firts_name = models.CharField("Nombres",max_length=100)
    last_name = models.CharField("Apellidos", max_length=100)
    job = models.CharField("Trabajo", max_length=1, choices=job_choices, default='4')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)




    def __str__(self):
        return f"{self.firts_name} {self.last_name} - {self.get_job_display()} - {self.departamento.name if self.departamento else 'Sin departamento'}"