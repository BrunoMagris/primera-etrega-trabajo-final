from django.urls import path

from App_1.views import formulario1, inicio, padre

urlpatterns = [
    path("padre/",padre),
    path("",inicio, name='Inicio'),
    path("form1/", formulario1),
]