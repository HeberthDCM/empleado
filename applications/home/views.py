from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba  # Import your model here if needed

# Create your views here.
class IndexView(TemplateView):
    template_name = "home/home.html"

class PruebaListView(ListView):
    #template_name = "home/lista.html"
    #def get_queryset(self):
    #    return ["A", "B", "C"]  
    
    #context_object_name = "lista_prueba"
    def get_queryset(self):
        return [{'nombre': item} for item in ['a', 'b', 'c']]

class ModeloPruebaListView(ListView):
    model =  Prueba  # Define your model here
    template_name = "home/pruebas.html"
    context_object_name = "lista_prueba"
    
 
 


