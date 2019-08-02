from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def cadastro_empresa(request):
    return render(request, 'cadastro_empresa.html')

def cadastro_candidato(request):
    return render(request, 'cadastro_candidato.html')