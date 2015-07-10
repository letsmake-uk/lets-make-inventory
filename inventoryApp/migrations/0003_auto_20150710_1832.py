# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventoryApp', '0002_auto_20150709_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=200)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(verbose_name=b'End date (Optional)', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventStock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(max_length=100, verbose_name=b'Link to item page', blank=True)),
                ('part', models.CharField(max_length=50, verbose_name=b'Part No.', blank=True)),
                ('ppu', models.FloatField(verbose_name=b'Price per unit')),
                ('max_del', models.CharField(max_length=100, verbose_name=b'Max delivery time', blank=True)),
                ('event', models.ForeignKey(to='inventoryApp.Event')),
                ('item', models.ForeignKey(to='inventoryApp.Item')),
                ('supplier', models.ForeignKey(to='inventoryApp.Supplier')),
            ],
        ),
        migrations.RemoveField(
            model_name='ownership',
            name='in_use',
        ),
        migrations.AddField(
            model_name='event',
            name='items',
            field=models.ManyToManyField(to='inventoryApp.Item', through='inventoryApp.EventStock'),
        ),
    ]
