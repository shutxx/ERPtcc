# Generated by Django 5.0.4 on 2024-04-23 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_alter_itensvenda_idvenda'),
    ]

    operations = [
        migrations.AddField(
            model_name='itensvenda',
            name='NomeProduto',
            field=models.CharField(default='default', max_length=255),
        ),
    ]