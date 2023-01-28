from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import request
from rest_framework.filters import SearchFilter, BaseFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet


from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class CustomSearchFilter(SearchFilter):
    search_param = "products"


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all().prefetch_related("positions")
    serializer_class = StockSerializer
    filter_backends = [CustomSearchFilter]
    search_fields = [
        "positions__product__id",
        "$positions__product__title",
        "$positions__product__description",
    ]
