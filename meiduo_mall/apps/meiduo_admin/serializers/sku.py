from rest_framework import serializers

from apps.goods.models import SKU, GoodsCategory, SPU


class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SKU
        fields = '__all__'


class GoodsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']


class SPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPU
        fields = ['id', 'name']