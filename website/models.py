from django.db import models
from django.urls import reverse

# Create your models here.

class Candidato(models.Model):

    GENEROS = (
        ('F','Feminino'),
        ('M','Masculino'),
        ('O','Outro'),
    )

    AREAS = (
        ('CMC', 'Comunicação'),
        ('SD', 'Saúde'),
        ('TEC', 'Tecnologia'),
        ('FIN', 'Financeiro'),
        ('ADM', 'Administração'),
        ('RH', 'RH'),
        ('JUR', 'Jurídica'),
        ('OTR', 'Outro')
    )

    ESCOLARIDADE = (
        ('EFI', 'Ensino Fundamental Incompleto'),
        ('EFC', 'Ensino Fundamental Cursando'),
        ('EFCO', 'Ensino Fundamental Completo'),
        ('EMI', 'Ensino Médio Incompleto'),
        ('EMC', 'Ensino Médio Cursando'),
        ('EMCO', 'Ensino Médio Completo'),
        ('ESI', 'Ensino Superior Incompleto'),
        ('ESC', 'Ensino Superior Cursando'),
        ('ESCO', 'Ensino Superior Completo'),
        ('P', 'Pós Graduação'),
        ('M', 'Mestrado'),
        ('D', 'Doutorado')
    )

    nome = models.CharField(
        max_length=255,
        verbose_name='Nome'
    )

    sobrenome = models.CharField(
        max_length=255,
        verbose_name='Sobrenome'
    )

    rne = models.CharField(
        max_length=255,
        verbose_name='Rne'
    )

    pais_de_origem = models.CharField(
        max_length=255,
        verbose_name='País de Origem'
    )

    data_nascimento = models.DateField()

    genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices = GENEROS
    )

    senha = models.CharField(
        max_length=255,
        verbose_name='Senha'
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    telefone = models.CharField(
        max_length=10,
        verbose_name='Telefone'
    )

    celular = models.CharField(
        max_length=11,
        verbose_name='Celular'
    )

    apresentacao = models.TextField(
        null=True,
        blank=True
    )

    area = models.CharField(
        verbose_name = 'Áreas',
        choices = AREAS,
        max_length=255
    )

    area_outros = models.CharField(
        null= True,
        blank=True,
        max_length=22,
        verbose_name = 'Caso outra, qual?'
    )

    formacao = models.TextField(
        verbose_name="Formação",
        blank=True
    )

    idioma = models.TextField(
        verbose_name= "Idioma",
        blank=True
    )

    historico = models.TextField(
        verbose_name="Histórico Profissional",
        blank=True
    )

    escolaridade = models.CharField(
        verbose_name = 'Escolaridade',
        choices = ESCOLARIDADE,
        max_length=255,
        default='SOME STRING'
    )

    # slug = models.SlugField(max_length=100)

    data_de_criacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + '' + self.sobrenome

    def get_absolute_url(self):
        
        return reverse('candid  atos:candidato', kwargs={'id': self.id})

class Empresa(models.Model):
    razao_social = models.CharField(
        max_length = 255,
        verbose_name = 'Razão Social'
    )

    email = models.EmailField(
        max_length=255,
        verbose_name='E-mail'
    )

    cnpj = models.CharField(
        max_length = 14,
        verbose_name = 'CNPJ'
    )

    senha = models.CharField(
        max_length = 255,
        verbose_name = 'Senha'
    )

    data_de_criacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.razao_social