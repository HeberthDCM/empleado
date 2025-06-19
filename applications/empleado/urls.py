from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path("listar-todo-empleados/",  views.listAllEmpleados.as_view(), name="list_all_empleados"),

    
]
