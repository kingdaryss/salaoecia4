# Generated by Django 3.0.6 on 2020-09-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0010_agendamento_motivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ean', models.CharField(max_length=200, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('estoque_comercial', models.IntegerField(null=True)),
                ('estoque_inicial', models.IntegerField(null=True)),
                ('valor_revenda', models.DecimalField(decimal_places=2, max_digits=14, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoUnidadeComercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('unidade', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]