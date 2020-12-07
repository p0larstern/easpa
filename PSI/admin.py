from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date_ordered',)
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(OrderItem,OrderItemAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    readonly_fields = ('date_added',)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
admin.site.register(Unprocessed_item)




