# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171205_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='row',
            name='element1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='element2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='element3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='element4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='element5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='row',
            name='row_length',
            field=models.IntegerField(null=True),
        ),
    ]
