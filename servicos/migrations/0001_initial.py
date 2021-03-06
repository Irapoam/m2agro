# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 02:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('safras', '0001_initial'),
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('nome', models.CharField(max_length=255)),
                ('data_inicial', models.DateField()),
                ('data_final', models.DateField()),
                ('custo_total', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServicoProduto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicos.Servico')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='produtos',
            field=models.ManyToManyField(through='servicos.ServicoProduto', to='produtos.Produto'),
        ),
        migrations.AddField(
            model_name='servico',
            name='safra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safras.Safra'),
        ),
    ]
