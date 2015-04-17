# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_moto_placa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=10)),
                ('moto', models.ForeignKey(to='core.Moto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
