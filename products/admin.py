# from django.contrib import admin
# from .models import Product, Category

# # Register your models here.

# admin.site.register(Category)

# from rest_framework import viewsets, permissions
# from .models import Product
# from .serializer import ProductSerializer

# class IsAdmin(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_staff

# class AdminProductView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [IsAdmin]