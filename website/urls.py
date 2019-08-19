from django.urls import path, include
from website.views import index, cadastro_candidato, cadastro_empresa, login, cadastro_cv, pagina_candidato, pagina_empresa, informacao_candidato


app_name = 'curriculos'

urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastro_empresa', cadastro_empresa),
    path('cadastro_candidato', cadastro_candidato),
    path('cadastro_cv', cadastro_cv),
    path('pagina_candidato', pagina_candidato),
    path('pagina_empresa', pagina_empresa),
    path('candidato/<int:id>', informacao_candidato, name ='curriculo')
]