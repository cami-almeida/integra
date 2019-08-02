from django.urls import path, include
from website.views import index, cadastro_candidato, cadastro_empresa, login

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastro_empresa', cadastro_empresa),
    path('cadastro_candidato', cadastro_candidato)
]