from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartView, CartAction, CheckoutView

router = DefaultRouter()
router.register(r'cart', CartView, basename='cart')

urlpatterns = [
    path('', include (router.urls)),
    path('add/<int:product_id>/', CartAction.as_view()),
    path('rest/<int:product_id>/', CartAction.as_view()),
    path('remove/<int:product_id>/', CartAction.as_view()),
    path('clear/', CartAction.as_view()),
    path('checkout/', CheckoutView.as_view()),
]
