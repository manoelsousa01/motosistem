# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150417_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moto',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterModelOptions(
            name='venda',
            options={'ordering': ['-pk'], 'verbose_name': 'Vendas'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='valor_total',
        ),
        migrations.AlterField(
            model_name='venda',
            name='valor_total',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
