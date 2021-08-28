from django.db import models

# В данном задании говорится об учете поставок и покупок товаров. 
# Поэтому тут исключены цена товара и учтено то, что покупка и поставка товара соверщается в момент сделки.

class Shop(models.Model):
    name = models.CharField(verbose_name='Название магазина', max_length=255)
    address = models.CharField(verbose_name='Адрес', max_length=255)

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey('shop.Shop', models.CASCADE, 'products_in_shop')
    name = models.CharField('Название товара', max_length=255)
    amount = models.PositiveIntegerField('Количество товара', default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class PurchaseRecord(models.Model):
    shop = models.ForeignKey('shop.Shop', models.CASCADE, 'purchases_in_shop')
    product = models.ForeignKey('shop.Product', models.CASCADE, 'product_purchase')
    quantity = models.PositiveIntegerField('Количество покупаемого товара', default=0)
    date = models.DateTimeField('Дата покупки', auto_now_add=True)

    class Meta:
        verbose_name = 'Учет покупки'
        verbose_name_plural = 'Учет покупок'

    def __str__(self):
        return self.date


class SupplyRecord(models.Model):  
    shop = models.ForeignKey('shop.Shop', models.CASCADE, 'supplies_in_shop')
    product = models.ForeignKey('shop.Product', models.CASCADE, 'product_supply')
    quantity = models.PositiveIntegerField('Количество поступаемого товара', default=0)
    date = models.DateTimeField('Дата поставки', auto_now_add=True)

    class Meta:
        verbose_name = 'Учет поставки'
        verbose_name_plural = 'Учет поставок'

    def __str__(self):
        return self.date

