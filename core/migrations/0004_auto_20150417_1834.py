# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abastecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField()),
                ('abastecedor', models.ForeignKey(to='core.Abastecedor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('endereco', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantidade', models.IntegerField()),
                ('valor_unitario', models.FloatField()),
                ('valor_total', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('disponibilidade', models.BooleanField()),
                ('quantidade', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('valor_total', models.FloatField()),
                ('cliente', models.ForeignKey(to='core.Cliente')),
                ('funcionario', models.ForeignKey(to='core.Funcionario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='peca',
            field=models.ForeignKey(to='core.Peca'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='venda',
            field=models.ForeignKey(to='core.Venda'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='compra',
            name='funcionario',
            field=models.ForeignKey(to='core.Funcionario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='abastecedor',
            name='peca',
            field=models.ForeignKey(to='core.Peca'),
            preserve_default=True,
        ),
    ]
