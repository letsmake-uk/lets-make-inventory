# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
                ('event', models.ForeignKey(to='inventoryApp.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Item name')),
                ('desc', models.CharField(max_length=400, verbose_name=b'Description of item', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_moved', models.DateField()),
                ('number_stored', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='inventoryApp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSupplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField(max_length=100, verbose_name=b'Link to item page', blank=True)),
                ('part', models.CharField(max_length=50, verbose_name=b'Part No.', blank=True)),
                ('ppu', models.FloatField(verbose_name=b'Price per unit')),
                ('max_del', models.CharField(max_length=100, verbose_name=b'Max delivery time', blank=True)),
                ('item', models.ForeignKey(to='inventoryApp.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Owner name')),
                ('contact', models.CharField(max_length=100, verbose_name=b'Owner contact', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_owned', models.IntegerField(default=0)),
                ('on_delivery', models.IntegerField(default=0)),
                ('item', models.ForeignKey(to='inventoryApp.Item')),
                ('owner', models.ForeignKey(to='inventoryApp.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='itemsupplier',
            name='supplier',
            field=models.ForeignKey(to='inventoryApp.Supplier'),
        ),
        migrations.AddField(
            model_name='itemlocation',
            name='location',
            field=models.ForeignKey(to='inventoryApp.Location'),
        ),
        migrations.AddField(
            model_name='item',
            name='locations',
            field=models.ManyToManyField(to='inventoryApp.Location', through='inventoryApp.ItemLocation'),
        ),
        migrations.AddField(
            model_name='item',
            name='owners',
            field=models.ManyToManyField(to='inventoryApp.Owner', through='inventoryApp.Ownership'),
        ),
        migrations.AddField(
            model_name='item',
            name='suppliers',
            field=models.ManyToManyField(to='inventoryApp.Supplier', through='inventoryApp.ItemSupplier'),
        ),
        migrations.AddField(
            model_name='eventstock',
            name='item',
            field=models.ForeignKey(to='inventoryApp.Item'),
        ),
        migrations.AddField(
            model_name='event',
            name='items',
            field=models.ManyToManyField(to='inventoryApp.Item', through='inventoryApp.EventStock'),
        ),
        migrations.AddField(
            model_name='event',
            name='organisation',
            field=models.ManyToManyField(to='inventoryApp.Owner'),
        ),
    ]
