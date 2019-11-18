from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('nuevo/alumno/', views.alta_alumno, name='Alta de alumnos'),
    path('nuevo/curso/', views.alta_curso, name='Alta de cursos'),
    path('<abrev_curso>/', views.vista_alumnos, name='Listado de alumnos'),
    path('', views.vista_cursos, name='Listado de cursos'),
#    path('login', views.alta_usuario, name='Alta de usuarios'),
]