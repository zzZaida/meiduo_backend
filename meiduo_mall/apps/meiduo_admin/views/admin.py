from django.contrib.auth.models import Group
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.admin import UserSerializer
from apps.meiduo_admin.serializers.group import GroupSerializer
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User
from rest_framework.generics import ListAPIView


class AdminModelViewSet(ModelViewSet):

    queryset = User.objects.filter(is_staff=True)

    serializer_class = UserSerializer

    pagination_class = PageNum


    # 在这里可以写
    # def create(self, request, *args, **kwargs):
    #
    #     pass


class GroupAllListAPIView(ListAPIView):

    queryset = Group.objects.all()

    serializer_class = GroupSerializer