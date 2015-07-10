# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='items',
        ),
        migrations.RemoveField(
            model_name='event',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='eventstock',
            name='event',
        ),
        migrations.RemoveField(
            model_name='eventstock',
            name='item',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventStock',
        ),
    ]
