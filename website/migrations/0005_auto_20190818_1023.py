# Generated by Django 2.2.4 on 2019-08-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_empresa_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='area',
            field=models.CharField(choices=[('CMC', 'Comunicação'), ('SD', 'Saúde'), ('TEC', 'Tecnologia'), ('FIN', 'Financeiro'), ('ADM', 'Administração'), ('RH', 'RH'), ('JUR', 'Jurídica'), ('OTR', 'Outro')], max_length=255, null=True, verbose_name='Áreas'),
        ),
    ]
