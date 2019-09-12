from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPU
from apps.meiduo_admin.serializers.spu import SPUSerializer
from apps.meiduo_admin.utils import PageNum


class SPUGoodsPAIView(ModelViewSet):

    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword:
            return SPU.objects.filter(name__contains=keyword)

        return SPU.objects.all()

    serializer_class = SPUSerializer

    pagination_class = PageNum