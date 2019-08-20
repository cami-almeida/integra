from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from website.models import Empresa, Candidato, Curriculo

# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    # função para deixar dois logins em uma unica index
    contexto = {}
    # verifica se o metodo é POST
    if request.method == 'POST':
        # verifica se o botão de login clicado pertence ao formulario de usuario
        if request.POST.get('submit') == 'ACESSAR CANDIDATO':
            # pega as informações do candidato apartir dos dados informados no formulario
            email_candidato = request.POST.get('email_candidato')
            senha_candidato = request.POST.get('senha')
            candidato = Candidato.objects.filter(email=email_candidato, senha=senha_candidato).first()
            # caso os dados forem invalidos/não existirem devolve uma mensagem de erro
            if candidato is None:
                contexto = {'msg':'login ou senha incorreto'}
            # caso tudo estiver correto redirecionaria para pagina em que o candidato altera suas informações
            # pagina inexistente
            else:
                contexto = {'candidato':candidato}
                return render(request,'cadastro_cv.html',contexto)


        # verifica se o botão de login clicado pertence ao formulario de empresa
        elif request.POST.get('submit') == 'ACESSAR EMPRESA':
            email_empresa = request.POST.get('email_empresa')
            senha_empresa = request.POST.get('senha')
            empresa = Empresa.objects.filter(email=email_empresa, senha=senha_empresa).first()
            if empresa is None:
                contexto = {'msg':'login ou senha incorreto'}
            else:
                candidatos = Candidato.objects.filter(ativo=True).all()
                curriculos = Curriculo.objects.filter(ativo=True).all()
                contexto = {'empresa':empresa, 'candidatos': candidatos, 'curriculos':curriculos}
                return render(request, 'pagina_empresa.html', contexto)
    return render(request, 'login.html',contexto)



def cadastro_empresa(request):
    if request.method == 'POST':
        empresa = Empresa()
        empresa.razao_social = request.POST.get('razao_social')
        empresa.cnpj = request.POST.get('cnpj')
        empresa.senha = request.POST.get('senha')
        empresa.email = request.POST.get('email')
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
        candidato.save()
        return render(request, 'login.html')
    return render(request, 'cadastro_candidato.html')


def cadastro_cv(request):   
    if request.method == 'POST':
        email_candidato = request.POST.get('email')
        candidato = Candidato.objects.filter(email=email_candidato).first()
        if candidato is not None:
            curriculo = Curriculo()
            curriculo.candidato = candidato
            curriculo.apresentacao = request.POST.get('apresentacao')
            curriculo.area = request.POST.get('area')
            curriculo.area_outros = request.POST.get('area_outros')
            curriculo.escolaridade = request.POST.get('escolaridade')
            curriculo.formacao = request.POST.get('formacao')
            curriculo.idioma = request.POST.get('idioma')
            curriculo.idioma_outros = request.POST.get('idioma_outros')
            curriculo.historico = request.POST.get('historico')
            curriculo.save()
            return redirect('/cadastro_cv')
    return render(request, 'index.html')

def pagina_candidato(request):
    candidatos = Candidato.objects.filter(ativo=True).all()
    contexto = {"candidatos":candidatos}
    return render(request, 'pagina_candidato.html',contexto)

# view para retornar lista de candidatos
def pagina_empresa(request):
    candidatos = Candidato.objects.filter(ativo=True).all()
    contexto = {"candidatos":candidatos}
    return render(request, 'pagina_empresa.html', contexto)

# view para retornar informações do candidato
def informacao_candidato(request, id):
    curriculo = get_object_or_404(Curriculo, id=id)
    contexto = {'curriculo':curriculo}
    return render(request, 'informacao_candidato.html', contexto)