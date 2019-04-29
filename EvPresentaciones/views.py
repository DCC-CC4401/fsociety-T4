from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def index(request, valor=False):
    return render(request, 'EvPresentaciones/Index.html', {'value': valor})


def testPage(request, value):
    """
    Pagina de prueba de la aplicacion.
    se ingresa a ella con /EvPresenataciones/testPage/0 o con /EvPresenataciones/testPage/1    
    """

    # Retornamos el el request, con el html asociado y un diccionario con los parametros que este necesita.
    return render(request, 'EvPresentaciones/testPage.html', {'value': value, 'list': range(1, value)})

# funciones Admin interface


def Cursos_admin(request):
    return render(request, 'EvPresentaciones/Admin_interface/Cursos_admin.html')


def Evaluaciones_admin(request):
    return render(request, 'EvPresentaciones/Admin_interface/Evaluaciones_admin.html')


def Evaluadores_admin(request):

    # obtenemos numero de evaluadores
    evaluadores = Usuario.objects.all()

    return render(request, 'EvPresentaciones/Admin_interface/Evaluadores_admin.html', {'evaluadores': evaluadores})


def Landing_page_admin(request):
    return render(request, 'EvPresentaciones/Admin_interface/Landing_page_admin.html')


def Rubricas_admin(request):
    return render(request, 'EvPresentaciones/Admin_interface/Rubricas_admin.html')

# funciones Evaluaciones


def Evaluacion(request):
    return render(request, 'EvPresentaciones/Eval_interface/evaluacion.html')


def Evaluacion_admin(request):
    return render(request, 'EvPresentaciones/Eval_interface/evaluacionadmin.html')


def Post_evaluacion(request):
    return render(request, 'EvPresentaciones/Eval_interface/postevaluacion.html')


def Post_evaluaciones_admin(request):
    return render(request, 'EvPresentaciones/Eval_interface/postevaluacionadmin.html')

# funciones Rubricas


def Ficha_Rubrica_admin(request):
    return render(request, 'EvPresentaciones/FichasRubricas/FichaRubricaAdministrador.html')


def Ficha_Rubrica_evaluador(request):
    return render(request, 'EvPresentaciones/FichasRubricas/FichaRubricaEvaluador.html')

# funciones resumen evaluacion


def Auth_summary(request):
    return render(request, 'EvPresentaciones/Summary_student/auth_summary.html')


def Summary(request):
    return render(request, 'EvPresentaciones/Summary_student/summary.html')


def LandingPage(request):

    user = request.POST.get('username', None)
    passw = request.POST.get('password', None)

    try:
        username = Usuario.objects.get(correo=user, contrasena=passw)
    except Usuario.DoesNotExist:
        return index(request, True)

    if username.isAdmin():
        return render(request, 'EvPresentaciones\Admin_interface/Landing_page_admin.html')
    else:
        return render(request, 'EvPresentaciones\Eval_interface/Landing_page_eval.html')


def HomeAdmin(request):
    return render(request, 'EvPresentaciones\Admin_interface/Landing_page_admin.html')

def agregarEvaluador(request):

    nombre = request.POST.get('usrname', None)
    apellido = request.POST.get('apellido', None)
    correo = request.POST.get('correo', None)

    contraseña = "RandomString"

    usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo,
                      contrasena=contraseña, esAdministrador=False)
    usuario.save()

    return Evaluadores_admin(request)
