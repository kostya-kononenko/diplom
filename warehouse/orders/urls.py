from orders.views import OrderViewSet, OrderItemViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename="order")
router.register(r'orderitems', OrderItemViewSet, basename="orderitem")

urlpatterns = [
    path('', include(router.urls)),
]
