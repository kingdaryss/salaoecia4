# Generated by Django 3.1.1 on 2020-09-22 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0015_produtounidadecomercial_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tipo',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='valor_revenda2',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]