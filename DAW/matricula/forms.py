from django.forms import ModelForm,CharField#,Form
from .models import Alumno
from .models import Curso
#import django.forms as forms alias
# Crea la clase del formulario
class AlumnoForm(ModelForm):
    class Meta:
        model = Alumno
        fields = ['dni', 'nombre', 'apellidos', 'imagen', 'curso']

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['abrev', 'denom', 'imagen']

#class FormLogin(Form):
#    user=CharField(max_length=20)
#    pwd=CharField(max_length=20)

    