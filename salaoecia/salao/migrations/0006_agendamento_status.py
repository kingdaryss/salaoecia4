# Generated by Django 3.0.6 on 2020-09-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0005_agendamento_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]