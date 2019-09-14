from django.contrib.auth.models import Group, Permission
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.group import GroupSerializer, PermissionSerializer
from apps.meiduo_admin.utils import PageNum

class GroupModelViewSet(ModelViewSet):

    queryset = Group.objects.all()

    serializer_class = GroupSerializer

    pagination_class = PageNum


class PermissionAllListAPIView(ListAPIView):

    queryset = Permission.objects.all()

    serializer_class = PermissionSerializer