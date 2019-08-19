# Generated by Django 2.2.4 on 2019-08-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190819_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='apresentacao',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='area',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='area_outros',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='escolaridade',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='formacao',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='historico',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='idioma',
        ),
        migrations.CreateModel(
            name='Curriculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apresentacao', models.TextField(blank=True, null=True)),
                ('area', models.CharField(choices=[('CMC', 'Comunicação'), ('SD', 'Saúde'), ('TEC', 'Tecnologia'), ('FIN', 'Financeiro'), ('ADM', 'Administração'), ('RH', 'RH'), ('JUR', 'Jurídica'), ('OTR', 'Outro')], max_length=255, null=True, verbose_name='Áreas')),
                ('area_outros', models.CharField(blank=True, max_length=22, null=True, verbose_name='Caso outra, qual?')),
                ('formacao', models.TextField(blank=True, verbose_name='Formação')),
                ('idioma', models.TextField(blank=True, verbose_name='Idioma')),
                ('historico', models.TextField(blank=True, verbose_name='Histórico Profissional')),
                ('escolaridade', models.CharField(choices=[('EFI', 'Ensino Fundamental Incompleto'), ('EFC', 'Ensino Fundamental Cursando'), ('EFCO', 'Ensino Fundamental Completo'), ('EMI', 'Ensino Médio Incompleto'), ('EMC', 'Ensino Médio Cursando'), ('EMCO', 'Ensino Médio Completo'), ('ESI', 'Ensino Superior Incompleto'), ('ESC', 'Ensino Superior Cursando'), ('ESCO', 'Ensino Superior Completo'), ('P', 'Pós Graduação'), ('M', 'Mestrado'), ('D', 'Doutorado')], default='SOME STRING', max_length=255, verbose_name='Escolaridade')),
                ('candidato', models.ForeignKey(on_delete=None, to='website.Candidato')),
            ],
        ),
    ]