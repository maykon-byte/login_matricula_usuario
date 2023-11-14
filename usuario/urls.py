from django.urls import path
from . import views

urlpatterns = [
    path('matricula/',views.matricula,name='matricula'),
    path('valida_matricula',views.valida_matricula,name='valida_matricula')
]
