# Generated by Django 3.0.6 on 2020-09-11 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_tempocontrato_dias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='tipo_endereco',
        ),
    ]
