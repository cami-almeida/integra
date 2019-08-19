from django.db import models
from django.urls import reverse

# Create your models here.

class Candidato(models.Model):

    GENEROS = (
        ('F','Feminino'),
        ('M','Masculino'),
        ('O','Outro'),
    )

    PAIS = (
	('AFE', 'Afeganistão'),
	('ADS', 'África do Sul'),
	('ALB','Albânia'),
	('ALE', 'Alemanha'),
    ('AND', 'Andorra'),
	('ANGO','Angola'),
	('ANG', 'Anguilla'),
	('AH','Antilhas Holandesas'),
	('ANT', 'Antárctida'),
	('AB', 'Antígua e Barbuda'),
	('ARG','Argentina'),
	('ARGE','Argélia'),
	('ARM', 'Armênia'),
	('ARU', 'Aruba'),
	('AS', 'Arábia Saudita'),
	('AUS', 'Austrália'),
	('AUST', 'Áustria'),
	('AZE', 'Azerbaijão'),
	('BAH', 'Bahamas'),
	('BAHR', 'Bahrein'),
	('BANG', 'Bangladesh'),
	('BARB','Barbados'),
	('BEL', 'Belize'),
	('BEN', 'Benim'),
	('BER', 'Bermudas'),
	('BIE', 'Bielorrússia'),
	('BOL', 'Bolívia'),
	('BOT', 'Botswana'),
	('BRU','Brunei'),
	('BUL','Bulgária'),
	('BURK','Burkina Faso'),
	('BURU','Burundi'),
	('BUT','Butão'),
	('BEL','Bélgica'),
	('BOSH','Bósnia e Herzegovina'),
	('CB','Cabo Verde'),
	('CAMA','Camarões'),
	('CAMB','Camboja'),
	('CAN','Canadá'),
	('CAT','Catar'),
	('CAZ','Cazaquistão'),
	('CHA','Chade'),
	('CHIL','Chile'),
	('CHIN','China'),
	('CHI','Chipre'),
	('COL','Colômbia'),
	('COM','Comores'),
	('CDN','Coreia do Norte'),
	('CDS','Coreia do Sul'),
	('CDM','Costa do Marfim'),
	('CR','Costa Rica'),
	('CRO','Croácia'),
	('CBA','Cuba'),
	('DIN','Dinamarca'),
	('DJI','Djibouti'),
	('DOM','Dominica'),
	('EGI','Egito'),
	('ES','El Salvador'),
	('EMA','Emirados Árabes Unidos'),
	('EQU','Equador'),
	('ERI','Eritreia'),
	('ESC','Escócia'),
	('ESL','Eslováquia'),
	('ESLOVE','Eslovênia'),
	('ESP','Espanha'),
	('EFM','Estados Federados da Micronésia'),
	('EUA', 'Estados Unidos'),
	('EST','Estônia'),
	('ETI','Etiópia'),
	('FIJ','Fiji'),
	('FIL','Filipinas'),
	('FIN','Finlândia'),
	('FRA','França'),
	('GAB','Gabão'),
	('GA','Gana'),
	('GE','Geórgia'),
	('GIB','Gibraltar'),
	('GRA','Granada'),
	('GRO', 'Gronelândia'),
	('GRE','Grécia'),
	('GUAD','Guadalupe'),
	('GUAM', 'Guam'),
	('GUAT','Guatemala'),
	('GUE','Guernesei'),
	('GUI','Guiana'),
	('GUIF','Guiana Francesa'),
	('GUE','Guiné'),
	('GUEEQ','Guiné Equatorial'),
	('GUIB','Guiné-Bissau'),
	('GAM','Gâmbia'),
	('HAI','Haiti'),
	('HON','Honduras'),
	('HK','Hong Kong'),
	('HUN','Hungria'),
	('IB','Ilha Bouvet'),
	('IM','Ilha de Man'),
	('IN','Ilha do Natal'),
	('IHIM','Ilha Heard e Ilhas McDonald'),
	('INOR','Ilha Norfolk'),
	('ICAY','Ilhas Cayman'),
	('ICO','Ilhas Cocos(Keeling)'),
    ('ICOOK','Ilhas Cook'),
	('IFE','Ilhas Feroé'),
	('IGSSS','Ilhas Geórgia do Sul e Sandwich do Sul'),
	('IMA', 'Ilhas Malvinas'),
	('IMAR','Ilhas Marshall'),
	('IMDEU', 'Ilhas Menores Distantes dos Estados Unidos'),
	('IS','Ilhas Salomão'),
	('IVA','Ilhas Virgens Americanas'),
	('IVB','Ilhas Virgens Britânicas'),
	('IAL','Ilhas Åland'),
	('INDO','Indonésia'),
	('ING','Inglaterra'),
	('INDI','Índia'),
	('IRAQ','Iraque'),
	('IRN','Irlanda do Norte'),
	('IRL','Irlanda'),
	('IRA','Irã'),
	('ISL','Islândia'),
	('ISR','Israel'),
	('ITA','Itália'),
	('IEM','Iêmen'),
	('JAM','Jamaica'),
	('JAP','Japão'),
	('JER','Jersey'),
	('JOR','Jordânia'),
	('KIR','Kiribati'),
	('KUW','Kuwait'),
	('LAO','Laos'),
	('LES','Lesoto'),
	('LET','Letônia'),
	('LIB','Libéria'),
	('LIE','Liechtenstein'),
	('LIT','Lituânia'),
	('LUX','Luxemburgo'),
	('LIBA','Líbano'),
	('LIBI','Líbia'),
	('MAC','Macau'),
	('MAC','Macedônia'),
	('MAD','Madagáscar'),
	('MALA','Malawi'),
	('MALD','Maldivas'),
	('MALI','Mali'),
	('MALTA','Malta'),
	('MALAS','Malásia'),
	('MARIS','Marianas Setentrionais'),
	('MARR','Marrocos'),
	('MART','Martinica'),
	('MAUR','Mauritânia'),
	('MAURI','Maurícia'),
	('MAYO','Mayotte'),
	('MOL','Moldávia'),
	('MON','Mongólia'),
	('MONT','Montenegro'),
	('MONTS','Montserrat'),
	('MOÇ','Moçambique'),
	('MYA','Myanmar'),
	('MEX','México'),
	('MON','Mônaco'),
	('NAM','Namíbia'),
	('NAU','Nauru'),
	('NEP','Nepal'),
	('NIC','Nicarágua'),
	('NIG','Nigéria'),
	('NIU','Niue'),
	('NOR','Noruega'),
	('NC','Nova Caledônia'),
	('NZ','Nova Zelândia'),
	('NIG','Níger'),
	('OMA','Omã'),
	('PAL','Palau'),
	('PALE','Palestina'),
	('PAN','Panamá'),
	('PNG','Papua-Nova Guiné'),
	('PAQ','Paquistão'),
	('PAR','Paraguai'),
	('PDG','País de Gales'),
	('PB','Países Baixos'),
	('PE','Peru'),
	('PIT','Pitcairn'),
	('PF','Polinésia Francesa'),
	('POL','Polônia'),
	('PR','Porto Rico'),
	('POR','Portugal'),
	('QUI','Quirguistão'),
	('QUE','Quênia'),
	('RU','Reino Unido'),
	('RCA','República Centro-Africana'),
	('RC','República Checa'),
	('RDC','República Democrática do Congo'),
	('RCO','República do Congo'),
	('RD','República Dominicana'),
	('REU','Reunião'),
	('ROM','Romênia'),
	('RUA','Ruanda'),
	('RUS','Rússia'),
	('SAA','Saara Ocidental'),
	('SM','Saint Martin'),
	('SB','Saint-Barthélemy'),
	('SPM','Saint-Pierre e Miquelon'),
	('SAM','Samoa Americana'),
	('SA','Samoa'),
	('SHATC','Santa Helena, Ascensão e Tristão da Cunha'),
	('SL','Santa Lúcia'),
	('SEN','Senegal'),
	('SLE','Serra Leoa'),
	('SEY','Seychelles'),
	('SIN','Singapura'),
	('SOM','Somália'),
	('SRI','Sri Lanka'),
	('SUAZ','Suazilândia'),
	('SUD','Sudão'),
	('SUR','Suriname'),
	('SUE','Suécia'),
	('SUI','Suíça'),
	('SVA','Svalbard e Jan Mayen'),
	('SCN','São Cristóvão e Nevis'),
	('SM','São Marino'),
	('STP','São Tomé e Príncipe'),
	('SVG','São Vicente e Granadinas'),
	('SERV','Sérvia'),
	('SIR','Síria'),
	('TAD','Tadjiquistão'),
	('TAI','Tailândia'),
	('TAIW','Taiwan'),
	('TAN','Tanzânia'),
	('TAAF','Terras Austrais e Antárticas Francesas'),
	('TBOI','Território Britânico do Oceano Índico'),
	('TL','Timor-Leste'),
	('TOG','Togo'),
	('TON','Tonga'),
	('TOQ','Toquelau'),
	('TRI','Trinidad e Tobago'),
	('TUN','Tunísia'),
	('TUR','Turcas e Caicos'),
	('TURQ','Turquemenistão'),
	('TURQUI','Turquia'),
	('TUV','Tuvalu'),
	('UCR','Ucrânia'),
	('UGA','Uganda'),
	('URU','Uruguai'),
	('UZB','Uzbequistão'),
	('VAN','Vanuatu'),
	('VAT','Vaticano'),
	('VEN','Venezuela'),
	('VIET','Vietname'),
	('WAF','Wallis e Futuna'),
	('ZIM','Zimbabwe'),
	('ZAM','Zâmbia')
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
        verbose_name='País de Origem',
        choices = PAIS,
		null= True
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
        verbose_name='Telefone',
        null= True
    )

    celular = models.CharField(
        max_length=11,
        verbose_name='Celular',
        null= True
    )
	
    data_de_criacao = models.DateField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    def get_absolute_url(self):
        return reverse('candidatos:candidato', kwargs={'id': self.id})


class Curriculo(models.Model):

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

	candidato = models.ForeignKey(
        Candidato, on_delete=None,
		null=True,
		verbose_name = 'Candidato',
    )

	apresentacao = models.TextField(
		verbose_name = 'Apresentação',
        null=True,
        blank=True
    )

	area = models.CharField(
        verbose_name = 'Áreas',
        choices = AREAS,
        max_length=255,
        null= True
    )

	area_outros = models.CharField(
        null= True,
        blank=True,
        max_length=22,
        verbose_name = 'Caso outra, qual?'
    )

	formacao = models.TextField(
		null= True,
        verbose_name="Formação",
        blank=True
    )

	idioma = models.TextField(
		null= True,
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