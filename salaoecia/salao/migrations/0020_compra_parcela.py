# Generated by Django 3.0.4 on 2020-11-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0019_salao'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='parcela',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
