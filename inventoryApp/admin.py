from django.contrib import admin

from .models import Location

from .models import Owner

from .models import Item

from .models import Ownership

from .models import ItemLocation

from .models import Supplier

from .models import ItemSupplier

class ItemLocationInline(admin.TabularInline):
    model = ItemLocation
    extra = 0

class OwnershipInline(admin.TabularInline):
    model = Ownership
    extra = 0

class ItemSupplierInline(admin.TabularInline):
    model = ItemSupplier
    extra = 0

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemLocationInline, ItemSupplierInline, OwnershipInline]
    list_display = ('name', 'total_items')

admin.site.register(Location)

admin.site.register(Owner)

admin.site.register(Supplier)

admin.site.register(Item, ItemAdmin)

#admin.site.register(Ownership)

#admin.site.register(ItemLocation)


#admin.site.register(ItemSupplier)
