from django import forms


class UsuarioFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)


class VideoFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)
    año = forms.CharField(max_length=4)
    descripcion = forms.CharField(max_length=300)


class MembresiaFormulario(forms.Form):

    nombre = forms.CharField(max_length=200)
    precio = forms.DecimalField(max_digits=5, decimal_places=2)
    Facturacion = forms.CharField(max_length=20)


class SolicitudFormulario(forms.Form):

    solicitud = forms.CharField(max_length=300)
    fecha = forms.CharField(max_length=30)
