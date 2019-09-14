from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Permission

from apps.meiduo_admin.serializers.permission import PermissionSerializer
from apps.meiduo_admin.utils import PageNum


class PermissionModelViewSet(ModelViewSet):

    queryset = Permission.objects.all()

    serializer_class = PermissionSerializer

    pagination_class = PageNum
