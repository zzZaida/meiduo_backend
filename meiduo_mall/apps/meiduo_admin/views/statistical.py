

"""
返回所有的用户
1.查询数据库获取数据
2.返回响应

"""

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.users.models import User
from datetime import datetime

class UserAllCountAPIView(APIView):

    def get(self, request):

        today = datetime.today()

        count = User.objects.all().count()

        return Response({
            'count': count,
            'today': today,

        })