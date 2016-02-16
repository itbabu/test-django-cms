# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('order', models.PositiveIntegerField(verbose_name='order', default=0)),
            ],
            options={
                'verbose_name': 'season',
                'ordering': ['order'],
                'verbose_name_plural': 'seasons',
            },
        ),
    ]
