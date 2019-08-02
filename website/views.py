from django.shortcuts import render
from website.models import Empresa, Candidato

# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def cadastro_empresa(request):
    if request.method == 'POST':
        empresa = Empresa()
        empresa.razao_social = request.POST.get('razao_social')
        empresa.cnpj = request.POST.get('cnpj')
        empresa.senha = request.POST.get('senha')
        empresa.save()
        print("empresa: ", empresa)
        return render(request, 'login.html')

    return render(request, 'cadastro_empresa.html')

def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html')