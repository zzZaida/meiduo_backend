from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.goods.models import SKUImage, SKU


class SKUImageSerializer(ModelSerializer):

    sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = ['id', 'sku', 'image']


#获取新增图片的SKU数据 序列化器
class SimpleSKUSerializer(ModelSerializer):

    class Meta:
        model = SKU
        fields = ['id', 'name']