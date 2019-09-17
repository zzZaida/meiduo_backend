from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPUSpecification
from apps.meiduo_admin.serializers.spec import SPUSpecificationSerializer
from apps.meiduo_admin.utils import PageNum


class SpecViewSet(ModelViewSet):

    queryset = SPUSpecification.objects.all()

    serializer_class = SPUSpecificationSerializer

    pagination_class = PageNum