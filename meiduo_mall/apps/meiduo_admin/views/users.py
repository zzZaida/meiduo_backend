
"""
需求(明确你要做什么):
    把所有的用户罗列出来

大体的步骤:
    1.先实现获取所有用户
        1.1 查询所有用户[User,User,User...]
        1.2 对象列表转化为字典列表
        1.3 返回数据
    2.再实现分页
    3.最后实现搜索

请求方式和路由
GET/meiduo_admin/users/
视图

"""

from rest_framework.generics import ListAPIView

from apps.meiduo_admin.serializers.users import UserSerializer
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User

"""
class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
"""



class UserListView(ListAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    pagination_class = PageNum

