from rest_framework import viewsets, permissions
from products.models import Product, Category
from .serializer import AdminProductSerializer, AdminCategorySerializer

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AdminProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = AdminProductSerializer
    permission_classes = [IsAdmin]

class AdminCategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = AdminCategorySerializer
    permission_classes = [IsAdmin]