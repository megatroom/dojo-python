from rest_framework import serializers
from .models import Product, Seller


class SellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'url']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'code',
                  'stock_size', 'seller', 'url']
