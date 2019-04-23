from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testPage/<int:value>', views.testPage, name='testPage'),
    
    path('Admin_interface/Cursos_admin',views.Cursos_admin, name='cursos_admin'),
    path('Admin_interface/Evaluaciones_admin',views.Evaluaciones_admin, name='evaluaciones_admin'),
    path('Admin_interface/Evaluadores_admin',views.Evaluadores_admin, name='evaluadores_admin'),
    path('Admin_interface/Landing_page_admin',views.Landing_page_admin, name='landing_page_admin'),
    path('Admin_interface/Rubricas_admin' ,views.Rubricas_admin, name='rubricas_admin'),
    
    path('Eval_interface/evaluacion',views.Evaluacion, name= 'evaluacion'),
    path('Eval_interface/evaluacionadmin',views.Evaluacion_admin, name= 'evaluacion_admin'),
    path('Eval_interface/postevaluacion',views.Post_evaluacion, name= 'post_evaluacion'),
    path('Eval_interface/postevalucionadmin',views.Post_evaluaciones_admin, name= 'post_evaluacion_admin'),

    path('FichasRubricas/FichaRubricaAdministrador',views.Ficha_Rubrica_admin, name='ficha_rubrica_admin'),
    path('FichasRubricas/FichaRubricaEvaluador', views.Ficha_Rubrica_evaluador, name='ficha_rubrica_eval'),

    path('Summary_student/auth_summary',views.Auth_summary, name ='auth_summary'),
    path('Summary_student/summary',views.Summary,name='summary'),

    


]