# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flavors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flavor', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=50)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Macaron',
            fields=[
                ('flavor', models.OneToOneField(primary_key=True, serialize=False, to='orders.Flavors')),
                ('quantity', models.IntegerField(default=3)),
                ('order', models.ForeignKey(to='orders.Order')),
            ],
        ),
    ]
