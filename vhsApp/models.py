from django.db import models


class Usuario(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField(default='')
    miembro_desde = models.DateField(auto_now_add=True)

    def __str__(self):

        return f"Usuario: {self.apellido} {self.nombre}"


class Video(models.Model):

    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    año = models.IntegerField(default=0)
    descripcion = models.TextField(default='')

    def __str__(self):

      
        return f"Video: {self.nombre} - Genero: {self.genero} - Año: {self.año}"


class Membresia(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    facturacion = models.CharField(max_length=20)

    def __str__(self):
        
        return f"Membresia: {self.nombre} - Precio: {self.precio}"


class Solicitar(models.Model):

    solicitud = models.TextField(default='')
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):

        return f"Solicitud: {self.solicitud} - Publicado: {self.fecha}"
