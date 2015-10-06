# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='flavors',
            name='description',
            field=models.CharField(default='Delicious!', max_length=200),
            preserve_default=False,
        ),
    ]
