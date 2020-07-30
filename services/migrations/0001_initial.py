# Generated by Django 2.2 on 2020-07-30 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre de la categoría', max_length=200, verbose_name='Nombre de la categoría')),
                ('icon', models.ImageField(blank=True, help_text='Icono de la categoría', null=True, upload_to='categories', verbose_name='Icono de la categoría')),
                ('parent_category', models.ForeignKey(help_text='Categoría padre', on_delete=django.db.models.deletion.DO_NOTHING, to='services.Category', verbose_name='Categoría padre')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nombre del servicio', max_length=200, verbose_name='Nombre del servicio')),
                ('description', models.TextField(blank=True, help_text='Descripción del servicio', null=True, verbose_name='Descripción del servicio')),
                ('photo', models.ImageField(blank=True, help_text='Foto del servicio', null=True, upload_to='services', verbose_name='Foto del servicio')),
                ('category', models.ForeignKey(help_text='Categoría del servicio', on_delete=django.db.models.deletion.DO_NOTHING, to='services.Category', verbose_name='Categoría del servicio')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['name'],
            },
        ),
    ]
