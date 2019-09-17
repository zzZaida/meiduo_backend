from rest_framework import serializers

from apps.goods.models import SPU, Brand, GoodsCategory


class SPUSerializer(serializers.ModelSerializer):

    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()

    category1_id = serializers.IntegerField()
    category2_id = serializers.IntegerField()
    category3_id = serializers.IntegerField()

    category1 = serializers.StringRelatedField(read_only=True)
    category2 = serializers.StringRelatedField(read_only=True)
    category3 = serializers.StringRelatedField(read_only=True)


    class Meta:
        model = SPU
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = ['id', 'name']
