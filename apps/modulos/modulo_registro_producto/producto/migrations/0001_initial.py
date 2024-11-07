# Generated by Django 4.2 on 2024-11-06 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=255)),
                ('descripcion_producto', models.TextField(blank=True, null=True)),
                ('precio_unitario', models.DecimalField(decimal_places=2, help_text='Precio del producto por unidad (ej. 15.50)', max_digits=10)),
                ('cantidad', models.IntegerField(default=0)),
                ('dimensiones', models.CharField(blank=True, max_length=255, null=True)),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso en kg', max_digits=10)),
                ('marca', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categoria.categoria', verbose_name='Categoría')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proveedor.proveedor', verbose_name='Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Productos',
            },
        ),
    ]