from django.test import TestCase

from BlogCoder.models import Autor, Blog

# Create your tests here.

class ViewTestCase(TestCase):

    def test_primero(self):
        autor = Autor.objects.create(nombre="Mario", apellido="Fernandez")
        cantidad_de_autores = Autor.objects.all()
        assert len(cantidad_de_autores) == 1
        

    def test_segundo(self):
        autor = Autor.objects.create(nombre="Juan", apellido="Pugliese")
        autor = Autor.objects.create(nombre="Agustin", apellido="Cisera")
        todos_los_autores = Autor.objects.all()
        assert len(todos_los_autores) == 2
        assert todos_los_autores[0].nombre == "Juan"
        assert todos_los_autores[1].apellido == "Cisera"



    def test_tercero(self):
        autor = Autor.objects.create(nombre="Oscar", apellido="Wilde")
        Blog.objects.create(
            autor = autor,
            titulo = "El Retrato de Dorian Gray",
            subtitulo = "Opiniones acerca de un libro excepcional",
            cuerpo = "Hoy le contaré de....",
        )

        cantidad_de_blogs = Blog.objects.all()
        assert len(cantidad_de_blogs) == 1
        

