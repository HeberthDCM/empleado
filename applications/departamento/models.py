from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField("Nombre",max_length=50, null=True, blank=True)
    surname = models.CharField("Nombre Corto",max_length=20, null=True, blank=True)
    anulate = models.BooleanField("Anulado",default=True)

    def __str__(self):
        return str(self.id) + " - " + self.name + " - " + self.surname + " - "