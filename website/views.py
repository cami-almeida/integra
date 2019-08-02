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
        return render(request, 'login.html')

    return render(request, 'cadastro_empresa.html')

def cadastro_candidato(request):
    if request.method == 'POST':
        candidato = Candidato()
        candidato.nome = request.POST.get('nome')
        candidato.sobrenome = request.POST.get('sobrenome')
        candidato.rne = request.POST.get('rne')
        candidato.pais_de_origem = request.POST.get('pais_de_origem')
        candidato.data_nascimento = request.POST.get('data_nascimento')
        candidato.genero = request.POST.get('genero')
        candidato.senha = request.POST.get('senha')
        candidato.email = request.POST.get('email')
        candidato.telefone = request.POST.get('telefone')
        candidato.celular = request.POST.get('celular')
        candidato.apresentacao = request.POST.get('apresentacao')
        candidato.apresentacao = request.POST.get('area')
        candidato.apresentacao = request.POST.get('area_outros')
        empresa.save()
        return render(request, 'login.html')
    return render(request, 'cadastro_candidato.html')