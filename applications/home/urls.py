from django.urls import path
from . import views

urlpatterns = [
    path("home/" , views.IndexView.as_view()),
    path("lista/", views.ListView.as_view(), name="lista_prueba"),
    path('home/lista-prueba/', views.ModeloPruebaListView.as_view(), name='lista_prueba'),
]