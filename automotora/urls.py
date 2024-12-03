from django.urls import path
from . import views  # Importa las vistas de la app automotora

urlpatterns = [
    path('index', views.index, name='index'),  # Ruta para la vista principal (home)
]