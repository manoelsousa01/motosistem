# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='placa',
            field=models.CharField(default=b'xxx-xxxx', max_length=8),
            preserve_default=True,
        ),
    ]
