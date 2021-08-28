from django.test import TestCase
from shop.views import PurchaseRecordView, SupplyRecordView
from shop.models import Product, Shop, PurchaseRecord, SupplyRecord


class FunctionalTest1(TestCase):
    def setUp(self):
        Shop.objects.create(name="Asman", address="Abay Street")
        Product.objects.create(shop="Asman", name="Milk", amount=150)
        PurchaseRecord.objects.create(shop="Asman", product="Milk", quantity=100)

    def test_purchase_works(self):
        shop = Shop.objects.get(name="Asman")
        product = Product.objects.get(name="Milk")
        purchase = PurchaseRecord.objects.get(shop=self.shop)
        response = purchase.purchase_counter()
        self.assertEqual(response.status, 200)
