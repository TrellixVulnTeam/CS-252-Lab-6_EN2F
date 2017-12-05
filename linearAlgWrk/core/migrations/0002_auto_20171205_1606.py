# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_steps', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_length', models.IntegerField()),
                ('element1', models.IntegerField()),
                ('element2', models.IntegerField()),
                ('element3', models.IntegerField()),
                ('element4', models.IntegerField()),
                ('element5', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_str', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Var',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_length', models.IntegerField()),
                ('col_length', models.IntegerField()),
                ('row1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row1', to='core.Row')),
                ('row2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row2', to='core.Row')),
                ('row3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row3', to='core.Row')),
                ('row4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row4', to='core.Row')),
                ('row5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='row5', to='core.Row')),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='endVar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endVar', to='core.Var'),
        ),
        migrations.AddField(
            model_name='step',
            name='startVar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startVar', to='core.Var'),
        ),
        migrations.AddField(
            model_name='output',
            name='step1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step1', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step10',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step10', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step11',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step11', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step12',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step12', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step2', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step3', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step4', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step5',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step5', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step6',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step6', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step7',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step7', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step8',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step8', to='core.Step'),
        ),
        migrations.AddField(
            model_name='output',
            name='step9',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='step9', to='core.Step'),
        ),
    ]
