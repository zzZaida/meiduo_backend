from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKU, GoodsCategory, SPU
from apps.meiduo_admin.serializers.sku import SKUSerializer, GoodsCategorySerializer, SPUSerializer
from apps.meiduo_admin.utils import PageNum


class SKUModelViewSet(ModelViewSet):

    def get_queryset(self):

        keyword = self.request.query_params.get('keyword')

        if keyword:
            return SKU.objects.filter(name__contains=keyword)

        return SKU.objects.all()

    serializer_class = SKUSerializer

    pagination_class = PageNum


"""
获取三级分类数据
GoodsCategory
GoodsCategory.objects.filter(parent_id__gt=37)
GoodsCategory.objects.filter(subs=None)



class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

"""
class ThreeCategoryListAPIView(ListAPIView):

    queryset = GoodsCategory.objects.filter()

    serializer_class = GoodsCategorySerializer


"""
获取所有的SPU的数据
"""
class SPUListAPIView(ListAPIView):

    queryset = SPU.objects.all()

    serializer_class = SPUSerializer