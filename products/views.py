from rest_framework import viewsets, filters
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

class ProductView(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['Category']
    search_fields = ['title']
    
    
    # filter_backends = [DjangoFilterBackend ,filters.SearchFilter]
    # search_fields = ['title']
    # filterset_fields = ['Category']
    
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = {
    #     'title': ['icontains'],
    # }