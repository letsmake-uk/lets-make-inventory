from django.db import models

# Basic objects, without relationships
class Location(models.Model):
    location = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.location

class Owner(models.Model):
    name = models.CharField('Owner name', max_length=50)
    contact = models.CharField('Owner contact', max_length = 100, blank = True)

    def __unicode__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length = 50)
    website = models.URLField(max_length = 100)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField('Item name', max_length=100)
    desc = models.CharField('Description of item', max_length=400, blank = True)
    locations = models.ManyToManyField(Location, through='ItemLocation')
    owners = models.ManyToManyField(Owner, through='Ownership')
    suppliers = models.ManyToManyField(Supplier, through='ItemSupplier')
    us = ['Louis', 'Nic', 'Lets Make']
    def ours(self):
        sum = 0
        ondel = 0
        ours = Ownership.objects.filter(
            item__id = self.id).filter(
            owner__name__in = self.us)
        for owns in ours:
            number = owns.number_owned
            sum += number
            ondel += owns.on_delivery
        return '%i (%i)' % (sum, ondel)
    ours.short_description = 'Ours (on-delivery)'

    def can_borrow(self):
        sum = 0
        ondel = 0
        not_ours = Ownership.objects.filter(
            item__id = self.id).exclude(
            owner__name__in = self.us)
        for owns in not_ours:
            number = owns.number_owned
            sum += number
            ondel += owns.on_delivery
        return '%i (%i)' % (sum, ondel)
    can_borrow.short_description = 'Others\'s items (on-delivery)'

# class Event(models.Model):
#     name = models.CharField(max_length=100)
#     place = models.CharField(max_length= 200)
#     start_date = models.DateField(blank=True)
#     end_date = models.DateField('End date (Optional)', blank=True)
#     items = models.ManyToManyField(Item, through='EventStock')
#     organisation = models.ManyToManyField(Owner)
#     def org(self):
#         return self.organisation.name
#     def __unicode__(self):
#         return self.name

# Relationship objects
class ItemLocation(models.Model):
    item = models.ForeignKey(Item)
    location = models.ForeignKey(Location)
    date_moved = models.DateField()
    number_stored = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.location.location

class Ownership(models.Model):
    owner = models.ForeignKey(Owner)
    item = models.ForeignKey(Item)
    number_owned = models.IntegerField(default = 0)
    on_delivery = models.IntegerField(default = 0)
#    in_use = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.owner.name

class ItemSupplier(models.Model):
    item = models.ForeignKey(Item)
    supplier = models.ForeignKey(Supplier)
    link = models.URLField('Link to item page', max_length=100, blank = True)
    part = models.CharField('Part No.', max_length=50, blank = True)
    ppu = models.FloatField('Price per unit')
    max_del = models.CharField('Max delivery time', max_length=100, blank = True)

    def __unicode__(self):
        return self.supplier.name

# class EventStock(models.Model):
#     event = models.ForeignKey(Event)
#     item = models.ForeignKey(Item)

#     def __unicode__(self):
#         return self.item.name
