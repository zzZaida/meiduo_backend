from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.order import OrderInfoSerializer
from apps.meiduo_admin.utils import PageNum
from apps.orders.models import OrderInfo


class OrderModelViewSet(ModelViewSet):

    queryset = OrderInfo.objects.all()

    serializer_class = OrderInfoSerializer

    pagination_class = PageNum