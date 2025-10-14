from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductView
from .views import AdminProductView, AdminCategoryView

router = DefaultRouter()
router.register(r'admin-products', AdminProductView, basename='admin-products')
router.register(r'admin-categories', AdminCategoryView, basename='admin-categories')


urlpatterns = [
    path('', include(router.urls))
]