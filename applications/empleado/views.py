from django.shortcuts import render
from django.views.generic import ListView, DetailView

#models
from .models import Empleados

# Create your views here.
class listAllEmpleados(ListView):
    model = Empleados
    template_name = 'empleado/list_all.html'
