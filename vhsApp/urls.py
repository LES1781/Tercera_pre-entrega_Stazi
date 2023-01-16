from django.urls import path

from vhsApp import views


app_name = 'vhsApp'

urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('usuarios/', views.listar_usuarios, name="Cursos"),
    path('videos/', views.listar_videos, name="Profesores"),
    path('membresias/', views.listar_membresias, name="Estudiantes"),
    path('buscar/', views.buscar, name="Buscar"),
]
