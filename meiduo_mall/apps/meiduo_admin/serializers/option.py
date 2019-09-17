from rest_framework import serializers

from apps.goods.models import SpecificationOption, SPUSpecification


class SpecificationOptionSerializer(serializers.ModelSerializer):

    spec_id = serializers.IntegerField()
    spec = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SpecificationOption
        fields = '__all__'


class SPUSpecificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPUSpecification
        fields = ['id', 'name']