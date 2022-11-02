from django.test import TestCase

from BlogCoder.models import Autor, Blog

# Create your tests here.

class ViewTestCase(TestCase):

    def primer_test(self):
        cantidad_de_autores = Autor.objects.all()
        assert len(cantidad_de_autores) == 3
        

    def segundo_test(self):
        autores = Autor.objects.all()
        assert autores[0].nombre == "Oscar"
        assert autores[0].apellido == "Wilde"


    def tercer_test(self):
        Blog.objects.create(
            autor="Oscar Wilde",
            titulo="El Retrato de Dorian Gray",
            subtitulo="Un joven apasionado",
            cuerpo="Esta es la historia de...",
        )
        cantidad_de_blogs = Blog.objects.all()
        assert len(cantidad_de_blogs) == 1

