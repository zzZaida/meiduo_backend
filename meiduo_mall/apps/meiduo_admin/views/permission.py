from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import Permission

from apps.meiduo_admin.serializers.permission import PermissionSerializer, ContentTypeSerializer
from apps.meiduo_admin.utils import PageNum


class PermissionModelViewSet(ModelViewSet):

    queryset = Permission.objects.all()

    serializer_class = PermissionSerializer

    pagination_class = PageNum


# 获取权限对应的 content_type(关联的模型)
from django.contrib.auth.models import ContentType
class ContentTypeAPIView(APIView):

    def get(self, request):

        queryset = ContentType.objects.all()

        s = ContentTypeSerializer(queryset, many=True)

        return Response(s.data)