from django.contrib import admin
from shop.models import Shop, Product, PurchaseRecord, SupplyRecord

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(PurchaseRecord)
admin.site.register(SupplyRecord)