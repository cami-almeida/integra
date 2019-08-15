from django.urls import path, include
from website.views import index, cadastro_candidato, cadastro_empresa, login, cadastro_cv, placeholder

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastro_empresa', cadastro_empresa),
    path('cadastro_candidato', cadastro_candidato),
    path('cadastro_cv', cadastro_cv),
    path('placeholder', placeholder)
]