from django.contrib import admin
from PSI.models import Product
from PSI.core import core
# Register your models here.
from .models import *

admin.site.register(Customer)
#admin.site.register(Product)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_ordered',)
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(OrderItem,OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
#admin.site.register(Unprocessed_item)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','pss','listed')
    actions = ['list_items']

    def list_items(self, request, queryset):
        g = core.generator(0,100,0,100,0,100,0,100)
        g.start()

        q1 = queryset.filter(listed='n')
        for item in q1:
            item.pss = g.get_psi(
                item.carbon_footprint,
                item.recyclability,
                item.biodegradability,
                item.waste_treated
            )
            item.listed = 'y'
            item.save()

        """
        self.message_user(request, ngettext(
            '%d product was successfully marked as listed.',
            '%d stories were successfully marked as listed.',
            q1,
        ) % q1, messages.SUCCESS)
        """

    list_items.short_description = "List unlisted items"
admin.site.register(Product,ProductAdmin)

