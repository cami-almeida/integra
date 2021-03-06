# Generated by Django 2.2.4 on 2019-08-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='formacao',
            field=models.TextField(blank=True, verbose_name='Formação'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='historico',
            field=models.TextField(blank=True, verbose_name='Histórico Profissional'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='idioma',
            field=models.TextField(blank=True, verbose_name='Idioma'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='area',
            field=models.CharField(choices=[('CMC', 'Comunicação'), ('SD', 'Saúde'), ('TEC', 'Tecnologia'), ('FIN', 'Financeiro'), ('ADM', 'Administração'), ('RH', 'RH'), ('JUR', 'Jurídica'), ('OTR', 'Outro')], max_length=255, verbose_name='Áreas'),
        ),
    ]
