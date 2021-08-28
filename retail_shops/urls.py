from django.contrib import admin
from django.urls import path
from shop.views import ShopViewSet, PurchaseRecordView, SupplyRecordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/stores/', ShopViewSet.as_view({'get': 'list'})),
    path('api/v1/stores/<int:pk>/', ShopViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/stores/<int:pk>/buy/', PurchaseRecordView.as_view({'post': 'purchase_counter'})),
    path('api/v1/stores/<int:pk>/add/', SupplyRecordView.as_view({'post': 'supply_counter'})),
]
