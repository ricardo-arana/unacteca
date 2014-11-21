# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editorial',
            options={'verbose_name': 'Editorial', 'verbose_name_plural': 'Editoriales'},
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='baja',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libro',
            name='portada',
            field=django_thumbs.db.models.ImageWithThumbsField(null=True, upload_to=b'portadas'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='libro',
            name='slug',
            field=models.SlugField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
