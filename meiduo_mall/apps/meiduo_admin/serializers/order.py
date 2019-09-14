from rest_framework import serializers

from apps.goods.models import SKU
from apps.orders.models import OrderInfo, OrderGoods

class OrderSKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = ['default_image', 'name', 'id']


class OrderGoodsSerializer(serializers.ModelSerializer):

    sku = OrderSKUSerializer()

    class Meta:
        model = OrderGoods
        fields = '__all__'

class OrderInfoSerializer(serializers.ModelSerializer):

    skus = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = '__all__'
