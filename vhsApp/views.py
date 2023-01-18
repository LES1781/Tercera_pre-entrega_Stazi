from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from vhsApp.models import Usuario, Video, Membresia, Solicitar
from vhsApp.forms import (
                          VideoFormulario, 
                          UsuarioFormulario,
                          MembresiaFormulario,
                          SolicitudFormulario,
                         )

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

def listar_solicitudes(request):

    contexto = {
        'solicitud': Solicitar.objects.all()
    }
    return render(
        request=request,
        template_name='vhsApp/lista_solicitudes.html',
        context=contexto,
    )

def buscar_videos(request):

      if  request.method == "POST":

            data = request.POST 
            videos = Video.objects.filter(
                Q(nombre__contains=data['busqueda']) | Q(genero__contains=data['busqueda'])
            )

            contexto = {'videos' : videos}

            return render(
                request=request,
                template_name='vhsApp/inicio.html',
                context=contexto,
            )

      else:
        
        respuesta = "No hay datos"

        return render(
            request=request,
            template_name='vhsApp/inicio.html',
            respuesta=respuesta,
            )

def crear_videos(request):

    if request.method == "POST":

        formulario = VideoFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            video = Video(
                          nombre=data['nombre'],
                          genero=data['genero'],
                          año=data['año'],
                          autor=data['autor'],
                          descripcion=data['descripcion']
                         )

            video.save()
            url_exitosa = reverse('listar_videos')
            return redirect(url_exitosa)

    else:
        formulario = VideoFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_videos.html',
        context={'formulario': formulario},
    )

def crear_usuarios(request):

    if request.method == "POST":

        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario = Usuario(
                              nombre=data['nombre'],
                              apellido=data['apellido'],
                              email=data['email']
                             )

            usuario.save()
            url_exitosa = reverse('listar_usuarios')
            return redirect(url_exitosa)

    else:
        formulario = UsuarioFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_usuario.html',
        context={'formulario': formulario},
    )

def crear_membresias(request):

    if request.method == "POST":

        formulario = MembresiaFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            membresia = Membresia(
                                  nombre=data['nombre'],
                                  precio=data['precio'],
                                  facturacion=data['facturacion']
                                 )

            membresia.save()
            url_exitosa = reverse('listar_membresias')
            return redirect(url_exitosa)

    else:
        formulario = MembresiaFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_membresia.html',
        context={'formulario': formulario},
    )

def crear_solicitudes(request):

    if request.method == "POST":

        formulario = SolicitudFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            solicitud = Solicitar(
                                  solicitud=data['solicitud'],
                                  fecha=data['fecha']
                                 )

            solicitud.save()
            url_exitosa = reverse('listar_solicitudes')
            return redirect(url_exitosa)

    else:
        formulario = SolicitudFormulario()

    return render(
        request=request,
        template_name='vhsApp/formulario_solicitudes.html',
        context={'formulario': formulario},
    )
