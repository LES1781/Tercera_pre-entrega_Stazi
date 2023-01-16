from django.db import models



class Usuario(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    miembro_desde = models.DateField(null=True)

    def __str__(self):

        return f"{self.apellido}, {self.nombre}"


class Video(models.Model):

    nombre = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    autoria = models.CharField(max_length=200)
    fecha = models.DateField(null=True)
    bio = models.TextField(null=True)

    def __str__(self):

        return f"{self.nombre}, {self.genero}, {self.fecha}"


class Membresia(models.Model):

    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    Facturacion = models.CharField(max_length=20)

    def __str__(self):
        
        return f"{self.nombre}, {self.precio}"


class Pregunta(models.Model):

    texto_pregunta = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):

        return self.texto_pregunta


class Choice(models.Model):

    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):

        return self.choice_text
