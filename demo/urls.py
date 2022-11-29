from django.urls import path
from .views import home, registrarCurso, eliminarCurso, edicionCurso, editarCurso

urlpatterns = [
    path('', home),
    path('registrarCurso/', registrarCurso),
    path('edicionCurso/<codigo>', edicionCurso),
    path('editarCurso/', editarCurso),
    path('eliminarCurso/<codigo>', eliminarCurso)
]