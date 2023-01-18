from django.urls import path

from vhsApp import views



urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('videos/', views.videos, name="videos"),
    path('usuarios/', views.listar_usuarios, name="listar_usuarios"),
    path('membresias/', views.listar_membresias, name="listar_membresias"),
    path('solicitudes/', views.listar_solicitudes, name="listar_solicitudes"),
    path('buscar/', views.buscar, name="buscar"),
    path('cargar_videos', views.cargar_videos, name="cargar_videos"),
    path('crear_usuarios', views.crear_usuarios, name="crear_usuarios"),
    path('crear_membresias', views.crear_membresias, name="crear_membresias"),
    path('crear_solicitudes', views.crear_solicitudes, name="crear_solicitudes"),
]
