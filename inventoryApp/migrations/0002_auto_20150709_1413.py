# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='in_use',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ownership',
            name='on_delivery',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
