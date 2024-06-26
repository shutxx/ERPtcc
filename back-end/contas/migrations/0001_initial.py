# Generated by Django 5.0.4 on 2024-04-27 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0003_alter_cliente_cpf'),
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DataVencimento', models.DateField()),
                ('DataPagamento', models.DateField(blank=True, null=True)),
                ('Pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContaPagar',
            fields=[
                ('conta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='contas.conta')),
                ('IdContaPagar', models.AutoField(primary_key=True, serialize=False)),
                ('IdFornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedores.fornecedor')),
            ],
            options={
                'verbose_name': 'ContaPagar',
                'verbose_name_plural': 'ContasPagar',
                'ordering': ['IdContaPagar'],
            },
            bases=('contas.conta',),
        ),
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('conta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='contas.conta')),
                ('IdContaReceber', models.AutoField(primary_key=True, serialize=False)),
                ('IdCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'ContaReceber',
                'verbose_name_plural': 'ContasReceber',
                'ordering': ['IdContaReceber'],
            },
            bases=('contas.conta',),
        ),
    ]
