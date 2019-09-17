from rest_framework import serializers

from apps.goods.models import SPUSpecification


class SPUSpecificationSerializer(serializers.ModelSerializer):

    spu_id = serializers.IntegerField()
    spu = serializers.StringRelatedField()

    class Meta:
        model = SPUSpecification
        fields = '__all__'