# Generated by Django 5.0.4 on 2024-08-18 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contas', '0001_initial'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contareceber',
            name='IdVenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendas.venda'),
        ),
    ]