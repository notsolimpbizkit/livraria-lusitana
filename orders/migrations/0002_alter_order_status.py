# Generated by Django 5.2 on 2025-06-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pendente', 'Pendente'), ('processamento', 'Processamento'), ('enviado', 'Enviado'), ('entregue', 'Entregue'), ('cancelado', 'Cancelado')], default='pendente', max_length=20),
        ),
    ]
