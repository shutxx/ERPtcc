# Generated by Django 5.0.4 on 2024-11-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_cpfcnpj_cliente_cpfoucnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Cidade',
            field=models.CharField(default='default', max_length=25),
        ),
    ]
