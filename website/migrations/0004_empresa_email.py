# Generated by Django 2.2.3 on 2019-08-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_candidato_escolaridade'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='email',
            field=models.EmailField(default='aa@gmail.com', max_length=255, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]