from rest_framework import serializers
from shop.models import Shop, Product, PurchaseRecord, SupplyRecord


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'amount')


class ShopSerializer(serializers.ModelSerializer):
    products_in_shop = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'address', 'products_in_shop')


class PurchaseRecordSerializer(serializers.ModelSerializer):
    purchases_in_shop = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseRecord
        fields = ('id', 'purchases_in_shop', 'product', 'quantity', 'date')

    # def create(self, validated_data):
    #     shop_data = validated_data.get('purchases_in_shop')
    #     product_data = validated_data.get('product_purchase')
    #     quantity = validated_data.get('quantity')
    #     shop = Shop.objects.get(pk=shop_data.id)
    #     product = Product.objects.get(pk=product_data.id)
    #     if product.amount < quantity:
    #         raise ValueError('Недостаточно товара для данной покупки')
    #     else:
    #         purchase = PurchaseRecord.objects.create(shop=shop, product=product, quantity=quantity)
    #         purchase.purch_calc()
    #         return purchase


class SupplyRecordSerializer(serializers.ModelSerializer):
    supplies_in_shop = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = PurchaseRecord
        fields = ('id', 'supplies_in_shop', 'product', 'quantity', 'date')

    # def create(self, validated_data):
    #     shop_data = validated_data.get('purchases_in_shop')
    #     product_data = validated_data.get('product_purchase')
    #     quantity = validated_data.get('quantity')
    #     shop = Shop.objects.get(pk=shop_data.id)
    #     product = Product.objects.get(pk=product_data.id)
    #     supply = SupplyRecord.objects.create(shop=shop, product=product, quantity=quantity)
    #     supply.suppl_calc()
    #     return supply
