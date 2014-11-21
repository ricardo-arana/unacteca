# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('texto', models.TextField()),
                ('postivos', models.IntegerField()),
                ('negativos', models.IntegerField()),
                ('fecha_publicacion', models.DateField(verbose_name=b'publicado')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=50)),
                ('edicion', models.CharField(max_length=50)),
                ('ano', models.CharField(max_length=4)),
                ('estado', models.CharField(max_length=1)),
                ('ingreso', models.DateField()),
                ('baja', models.DateField()),
            ],
            options={
                'verbose_name': 'Ejemplar',
                'verbose_name_plural': 'Ejemplares',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'etiqueta',
                'verbose_name_plural': 'etiquetas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('iniciales', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('portada', models.ImageField(upload_to=b'')),
                ('calificacion', models.FloatField()),
                ('slug', models.SlugField()),
                ('autor', models.ForeignKey(to='biblioteca.Autor')),
                ('editorial', models.ForeignKey(to='biblioteca.Editorial')),
                ('etiqueta', models.ManyToManyField(to='biblioteca.Etiqueta')),
                ('idioma', models.ForeignKey(to='biblioteca.Idioma')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mora',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dias', models.IntegerField()),
                ('costoxdia', models.FloatField()),
                ('estado', models.CharField(max_length=1)),
                ('Usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mora',
                'verbose_name_plural': 'Moras',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolucion', models.DateField()),
                ('estado', models.CharField(max_length=1)),
                ('dias_mora', models.IntegerField(default=0)),
                ('ejemplar', models.ForeignKey(to='biblioteca.Ejemplar')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prestamo',
                'verbose_name_plural': 'Prestamos',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='libro',
            name='materia',
            field=models.ForeignKey(to='biblioteca.Materia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ejemplar',
            name='libro',
            field=models.ForeignKey(to='biblioteca.Libro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='libro',
            field=models.ForeignKey(to='biblioteca.Libro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
