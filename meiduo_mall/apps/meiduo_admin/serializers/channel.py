from rest_framework import serializers

from apps.goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory


class GoodsChannelSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()

    group = serializers.StringRelatedField(read_only=True)
    group_id = serializers.IntegerField()

    class Meta:
        model = GoodsChannel
        fields = '__all__'


class GoodsChannelGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsChannelGroup
        fields = ['id', 'name']


class GoodsCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'