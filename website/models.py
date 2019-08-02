from django.db import models

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

    data_de_criacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + '' + self.sobrenome

class Empresa(models.Model):
    razao_social = models.CharField(
        max_length = 255,
        verbose_name = 'Razão Social'
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