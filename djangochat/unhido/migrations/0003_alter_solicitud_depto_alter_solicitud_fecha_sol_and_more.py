# Generated by Django 4.0.2 on 2023-05-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unhido', '0002_solicitud_valida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='depto',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_sol',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='justifica',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='objeto',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='prioridad',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='rubro',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='unidad',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='valida',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
