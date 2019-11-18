from django.shortcuts import render, redirect
from .models import Alumno, Curso
from .forms import AlumnoForm,CursoForm#,FormLogin
#from django.contrib.auth import authenticate,login


def vista_alumnos(request, abrev_curso):
    alumnos = Alumno.objects.filter(curso__abrev=abrev_curso)
    return render(request, "lista_alumnos.html", {'alumnos':alumnos})

def vista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "lista_cursos.html", {'cursos':cursos})

def alta_alumno(request):
    if request.POST:
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_alumno = form.save()
            print(f"Se ha creado a: {nuevo_alumno}")
            return redirect('/'+nuevo_alumno.curso.abrev)
        else:
            return render(request, "alta_alumno.html", {'form': form})
    else:
        form = AlumnoForm()
        return render(request, "alta_alumno.html", {'form': form})
            

def alta_curso(request):
    if request.POST:
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            nuevo_curso = form.save()
            print(f"Se ha creado a: {nuevo_curso}")
            return redirect('/'+nuevo_curso.abrev)
        else:
            return render(request, "alta_curso.html", {'form': form})
    else:
        form = CursoForm()
        return render(request, "alta_curso.html", {'form': form})



#def alta_usuario(request):
#    if request.method=='POST' and request.POST['user'] != 'root':
#        form = FormLogin(request.POST)
#
#        username=request.POST['user']
#        password=request.POST['pwd']
#        user=authenticate(request,username=username,password=password)
#        if user is not None:
#            login(request,user)
#            return redirect("/")
#        
 #       else:
  #          return render(request, "login.html", {'form': form})
   # else:
    #    form = FormLogin()
     #   return render(request, "login.html", {'form': form})
   