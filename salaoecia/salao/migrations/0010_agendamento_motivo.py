# Generated by Django 3.0.6 on 2020-09-03 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0009_agendamento_funcionario_cancelou'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='motivo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='salao.MotivosAgendamento'),
        ),
    ]
