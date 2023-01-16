from django.shortcuts import render, redirect
from django.urls import reverse

from vhsApp.models import Usuario, Video, Membresia

def inicio(request):
    return render(
        request=request,
        template_name='vhsApp/inicio.html',
    )


def listar_usuarios(request):

    contexto = {
        'usuarios': Usuario.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_usuarios.html',
        context=contexto,
    )

def listar_videos(request):

    contexto = {
        'videos': Video.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_videos.html',
        context=contexto,
    )

def listar_membresias(request):

    contexto = {
        'membresias': Membresia.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_membresias.html',
        context=contexto,
    )

def buscar(request):

      if  request.GET["video"]:
            video = request.GET['video'] 
            videos = Video.objects.filter(video__icontains=video)

            return render(request, "AppCoder/inicio.html", {"videos":videos, "video":video})

      else:
        respuesta = "No enviaste datos"
        return render(request, "vhsApp/inicio.html", {"respuesta":respuesta})

