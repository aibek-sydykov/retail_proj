from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from shop.serializers import ProductSerializer, ShopSerializer, PurchaseRecordSerializer, SupplyRecordSerializer
from shop.models import Shop, Product, PurchaseRecord, SupplyRecord
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.prefetch_related('products_in_shop').all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'


class PurchaseRecordView(ModelViewSet):
    serializer_class =  PurchaseRecordSerializer
    queryset = PurchaseRecord.objects.select_for_update().prefetch_related('purchases_in_shop', 'product_purchase')
    lookup_field = 'pk'

    @action(detail=True, methods=['post'])
    def purchase_counter(self, request, pk=None):
        product_data = request.data.get('product')
        quantity = int(request.data.get('quantity'))
        shop = Shop.objects.get(pk=pk)
        product = Product.objects.get(pk=product_data)
        serializer = PurchaseRecordSerializer(data=request.data)
        if product.shop == shop:
            if product.amount < quantity:
                return Response({'status': 'Недостаточно товаров для покупки'})
            else:
                product.amount -= quantity
                purchase = PurchaseRecord.objects.create(shop=shop, product=product, quantity=quantity)
                product.save()
                if serializer.is_valid():
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Данного товара в магазине нет'}) 
        

class SupplyRecordView(ModelViewSet):
    serializer_class =  SupplyRecordSerializer
    queryset = SupplyRecord.objects.prefetch_related('supplies_in_shop', 'product_supply')
    lookup_field = 'pk'

    @action(detail=True, methods=['post'])
    def supply_counter(self, request, pk=None):
        product_data = request.data.get('product')
        quantity = int(request.data.get('quantity'))
        shop = Shop.objects.get(pk=pk)
        product = Product.objects.get(pk=product_data)
        serializer = SupplyRecordSerializer(data=request.data)
        if product.shop == shop:
            product.amount += quantity
            supply = SupplyRecord.objects.create(shop=shop, product=product, quantity=quantity)
            product.save()
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            new_product = Product.objects.create(shop=shop, name=product.name, amount=quantity)
            new_supply = SupplyRecord.objects.create(shop=shop, product=new_product, quantity=quantity)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


