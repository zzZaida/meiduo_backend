from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SpecificationOption, SPUSpecification
from apps.meiduo_admin.serializers.option import SpecificationOptionSerializer, SPUSpecificationSerializer
from apps.meiduo_admin.utils import PageNum


class SpecificationOptionViewSet(ModelViewSet):

    queryset = SpecificationOption.objects.all()

    serializer_class = SpecificationOptionSerializer

    pagination_class = PageNum


# 获取规格信息
class SPUSpecificationAPIView(ListAPIView):

    queryset = SPUSpecification.objects.all()

    serializer_class = SPUSpecificationSerializer