# Generated by Django 3.0.4 on 2020-11-07 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0020_compra_parcela'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='vlr_parcelado',
            field=models.DecimalField(decimal_places=2, max_digits=14, null=True),
        ),
    ]
