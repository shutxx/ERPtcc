# Generated by Django 5.0.4 on 2024-04-26 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_alter_itenscompra_qtdproduto'),
    ]

    operations = [
        migrations.AddField(
            model_name='itenscompra',
            name='NomeProduto',
            field=models.CharField(default='default', max_length=255),
        ),
    ]
