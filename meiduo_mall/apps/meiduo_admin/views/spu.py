from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPU, Brand, GoodsCategory
from apps.meiduo_admin.serializers.spu import SPUSerializer, BrandSerializer, CategorySerializer
from apps.meiduo_admin.utils import PageNum


class SPUGoodsViewSet(ModelViewSet):

    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword:
            return SPU.objects.filter(name__contains=keyword)

        return SPU.objects.all()

    serializer_class = SPUSerializer

    pagination_class = PageNum


# 获取品牌信息
class SPUBrandAPIView(ListAPIView):

    queryset = Brand.objects.all()

    serializer_class = BrandSerializer


# 获取一级分类信息
class ChannelCategorysView(ListAPIView):

    queryset = GoodsCategory.objects.filter(parent=None)

    serializer_class = CategorySerializer

# 获取二级 三级分类信息
class ChannelCategoriesView(ListAPIView):

    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        return GoodsCategory.objects.filter(parent_id=id)

    serializer_class = CategorySerializer


