# Generated by Django 2.2.4 on 2019-08-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20190819_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='idioma_outros',
            field=models.CharField(blank=True, max_length=22, null=True, verbose_name='Caso outra, qual?'),
        ),
        migrations.AlterField(
            model_name='curriculo',
            name='idioma',
            field=models.TextField(blank=True, choices=[('INGLES', 'INGLÊS'), ('ESPANHOL', 'ESPANHOL'), ('FRANCES', 'FRANCÊS'), ('OTR', 'OUTRO')], null=True, verbose_name='Idioma'),
        ),
    ]
