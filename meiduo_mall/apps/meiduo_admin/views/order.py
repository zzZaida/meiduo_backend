from rest_framework.decorators import action
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

    @action(methods=['PUT'],detail=True)
    def status(self,request,pk):
        # 1.查询订单
        try:
            order=OrderInfo.objects.get(order_id=pk)
        except OrderInfo.DoesNotExist:
            from rest_framework import status
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # order=self.get_object()
        # 2.修改订单状态
        order.status=request.data.get('status')
        order.save()
        #3.返回相应
        return Response({
            'order_id':pk,
            'status':order.status
        })


    """
    GET
    {
      "order_id": "20190909155657000000003",
      "create_time": "2019-09-09T15:56:57.524510+08:00",
      "update_time": "2019-09-09T15:57:02.595491+08:00",
      "total_count": 1,
      "total_amount": "11.00",
      "freight": "10.00",
      "pay_method": 2,
      "status": 1,
      "user": 3,
      "address": 4,
      "goods":[{},{},{},{}]
    }
    """