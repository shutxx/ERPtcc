# Generated by Django 5.0.4 on 2024-04-25 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenscompra',
            name='QtdProduto',
            field=models.IntegerField(),
        ),
    ]
