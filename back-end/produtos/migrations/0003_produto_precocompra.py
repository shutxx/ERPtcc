# Generated by Django 5.0.4 on 2024-12-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_alter_produto_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='PrecoCompra',
            field=models.FloatField(default=0.0, max_length=10),
        ),
    ]