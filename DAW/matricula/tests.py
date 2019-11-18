from django.test import TestCase
from .models import Curso,Alumno

class CursoTestCase(TestCase):
    def setUp(self):
        Curso.objects.create(abrev="2DAW", denom="2ºDAW",imagen="fotos/asgard.jpg")

    def test_Cursos(self):
        DAW=Curso.objects.get(abrev="2DAW")
        eso=Curso.objects.get(imagen="fotos/asgard.jpg")
        self.assertEqual(DAW.__str__(),"2ºDAW")
        self.assertEqual(eso.imagen,"fotos/asgard.jpg")

class AlumnoTestCase(TestCase):
    def setUp(self):
        Alumno.objects.create(dni="7717881P",nombre="Manue",apellidos="Rosendo",imagen="fotos/asgard.jpg")

    def test_Alumnos(self):
        dniN=Alumno.objects.get(dni="7717881P")
        self.assertEqual(dniN.dni,"7717881P")
