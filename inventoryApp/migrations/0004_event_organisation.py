# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0003_auto_20150710_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organisation',
            field=models.ManyToManyField(to='inventoryApp.Owner'),
        ),
    ]
