# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_addres', models.CharField(max_length=15)),
                ('neighbor', models.CharField(max_length=50)),
            ],
        ),
    ]
