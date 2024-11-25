# Generated by Django 4.2 on 2024-11-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_metodo_pago', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Metodos de Pago',
            },
        ),
    ]
