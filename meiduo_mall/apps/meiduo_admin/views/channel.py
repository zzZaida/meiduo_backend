from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import GoodsChannel, GoodsChannelGroup, GoodsCategory
from apps.meiduo_admin.serializers.channel import GoodsChannelSerializer, GoodsChannelGroupSerializer, \
    GoodsCategorySerializer
from apps.meiduo_admin.utils import PageNum


class GoodsChannelViewSet(ModelViewSet):

    queryset = GoodsChannel.objects.all()

    serializer_class = GoodsChannelSerializer

    pagination_class = PageNum


class GoodsChannelGroupAPIView(ListAPIView):

    queryset = GoodsChannelGroup.objects.all()

    serializer_class = GoodsChannelGroupSerializer


class GoodsCategoryAPIView(ListAPIView):

    queryset = GoodsCategory.objects.filter(parent_id=None)

    serializer_class = GoodsCategorySerializer
