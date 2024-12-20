# Generated by Django 4.2 on 2024-11-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repartidor',
            fields=[
                ('id_repartidor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('cedula', models.CharField(max_length=50, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_licencia', models.CharField(max_length=50, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Repartidores',
            },
        ),
    ]
