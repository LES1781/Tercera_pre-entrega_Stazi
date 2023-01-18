from django.shortcuts import render, redirect
from django.urls import reverse


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

def videos(request):

    if request.method == 'POST':
        formulario = VideoFormulario(request.POST)
        print(formulario)
        
        if formulario.is_valid():
            
            informacion = formulario.cleaned_data

            video = Video(
                nombre=informacion['nombre'], 
                genero=informacion['genero'],
                autor=informacion['autor'],
                año=informacion['año'],
            )

            video.save()
            return render(request, "vhsApp/inicio.html")
        
        else:
            
            formulario = VideoFormulario()
            return render(request, "vhsApp/videos.html", {"formulario":formulario})

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

def buscar(request):

      if  request.GET["video"]:
            video = request.GET['video'] 
            videos = Video.objects.filter(video__icontains=video)

            return render(request, "vhsApp/inicio.html", {"videos":videos, "video":video})

      else:
        respuesta = "No enviaste datos"

        return render(request, "vhsApp/inicio.html", {"respuesta":respuesta})

def cargar_videos(request):

    if request.method == "POST":
        formulario = VideoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Video(nombre=data['nombre'], genero=data['genero'])
            curso.save()
            url_exitosa = reverse('videos')
            return redirect(url_exitosa)
    else:
        formulario = VideoFormulario()
    return render(
        request=request,
        template_name='vhsApp/formulario_video.html',
        context={'formulario': formulario},
    )

def crear_usuarios(request):

    if request.method == "POST":

        formulario = UsuarioFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data
            usuario = Usuario(nombre=data['nombre'], apellido=data['apellido'], email=['email'])
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
            membresia = Membresia(nombre=data['nombre'], precio=data['precio'], facturacion=['facturacion'])
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
            solicitud = Solicitar(solicitud=data['solicitud'], fecha=data['fecha'])
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
