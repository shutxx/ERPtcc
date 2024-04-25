# Generated by Django 5.0.4 on 2024-04-25 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fornecedores', '0001_initial'),
        ('produtos', '0002_alter_produto_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('IdCompra', models.AutoField(primary_key=True, serialize=False)),
                ('DataCompra', models.DateField()),
                ('ValorTotal', models.FloatField(max_length=10)),
                ('IdFornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'ordering': ['IdCompra'],
            },
        ),
        migrations.CreateModel(
            name='ItensCompra',
            fields=[
                ('IdItensCompra', models.AutoField(primary_key=True, serialize=False)),
                ('ValorUnitario', models.FloatField(max_length=10)),
                ('QtdProduto', models.IntegerField(max_length=10)),
                ('ValorTotal', models.FloatField(max_length=10)),
                ('IdCompra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens_compra', to='compras.compra')),
                ('IdProduto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
            options={
                'verbose_name': 'ItenCompra',
                'verbose_name_plural': 'ItensCompra',
                'ordering': ['IdItensCompra'],
            },
        ),
    ]