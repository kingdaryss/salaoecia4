# Generated by Django 3.0.4 on 2020-11-07 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_user_fx_salario'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_bloqueado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='perc_comissao',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tentativas_login',
            field=models.IntegerField(null=True),
        ),
    ]
