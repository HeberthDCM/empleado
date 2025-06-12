from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField("Nombre",max_length=50)
    surname = models.CharField("Nombre COrto",max_length=20)
    anulate = models.BooleanField("Anulado",default=True)

    def __str__(self):
        return self.id + " - " + self.name + " - " + self.surname + " - " + str(self.anulate)