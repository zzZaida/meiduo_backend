from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKU, GoodsCategory, SPU, SPUSpecification
from apps.meiduo_admin.serializers.sku import SKUSerializer, GoodsCategorySerializer, SPUSerializer, \
    SPUSpecificationSerializer
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


"""
需求:
    当我们选择某一个SPU之后,先获取商品所对应 的规格(颜色,内存)
    确定了规格之后,再获取规格选项信息(颜色:金色)

大体步骤:
    1.获取SPU的id
    2.SPUSpecification
    3.SpecificationOption

请求方式:
    GET  meiduo_admin/goods/(?P<pk>\d+)/specs/
"""

# class SPUSpecsAPIView(APIView):
#
#     def get(self, request, pk):
#
#         specs = SPUSpecification.objects.filter(spu_id=pk)
#
#         s = SPUSpecificationSerializer(specs, many=True)
#
#         return Response(s.data)

from rest_framework.generics import ListAPIView,RetrieveAPIView
class SPUSpecsAPIView(ListAPIView):

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return SPUSpecification.objects.filter(spu_id=pk)


    serializer_class = SPUSpecificationSerializer