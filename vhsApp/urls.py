from django.urls import path

from vhsApp import views



urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('videos/', views.listar_videos, name="listar_videos"),
    path('usuarios/', views.listar_usuarios, name="listar_usuarios"),
    path('membresias/', views.listar_membresias, name="listar_membresias"),
    path('solicitudes/', views.listar_solicitudes, name="listar_solicitudes"),
    path('buscar_videos/', views.buscar_videos, name="buscar.videos"),
    path('crear_videos', views.crear_videos, name="crear_videos"),
    path('crear_usuarios', views.crear_usuarios, name="crear_usuarios"),
    path('crear_membresias', views.crear_membresias, name="crear_membresias"),
    path('crear_solicitudes', views.crear_solicitudes, name="crear_solicitudes"),
]
