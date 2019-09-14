from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.order import OrderInfoSerializer
from apps.meiduo_admin.utils import PageNum
from apps.orders.models import OrderInfo


class OrderModelViewSet(ModelViewSet):

    queryset = OrderInfo.objects.all()

    serializer_class = OrderInfoSerializer

    pagination_class = PageNum

    def destroy(self, request, *args, **kwargs):

        return Response({'msg': '妖怪,吃俺老孙一棒,敢删除我的数据!'})
