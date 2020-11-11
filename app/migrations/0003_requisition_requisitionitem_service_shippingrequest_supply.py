# Generated by Django 3.1 on 2020-11-11 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201111_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.BooleanField(default=False)),
                ('all_terrain_vehicle', models.BooleanField(default=False)),
                ('required_ad', models.DateTimeField(auto_now_add=True)),
                ('fulfilled_at', models.DateTimeField()),
                ('created_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shelter', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='app.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('enabled', models.BooleanField(default=True)),
                ('required_by', models.CharField(choices=[('all', 'Todos'), ('baby', 'Bebes'), ('children', 'Niños'), ('baby', 'Bebes'), ('men', 'Hombres'), ('women', 'Mujeres'), ('women', 'Tercera edad')], max_length=50)),
                ('priority', models.CharField(choices=[('minimal', 'Minima'), ('medium', 'Media'), ('high', 'Alta'), ('highest', 'La mas alta')], max_length=50)),
                ('created_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('assigned', 'Asignada'), ('done', 'Hecho'), ('cancelled', 'Cancelada')], max_length=50)),
                ('scheduled_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shelter', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='app.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('assigned', 'Asignada'), ('done', 'Hecho'), ('cancelled', 'Cancelada')], max_length=50)),
                ('volunteer', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('supplies', 'Insumos'), ('medical', 'Medico')], max_length=50)),
                ('required_ad', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('shelter', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='app.shelter')),
            ],
        ),
        migrations.CreateModel(
            name='RequisitionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desired_qty', models.IntegerField()),
                ('provided_qty', models.IntegerField()),
                ('created_by', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=40, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('requisition', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='app.requisition')),
                ('supply', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.PROTECT, to='app.supply')),
            ],
        ),
    ]
