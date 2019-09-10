
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
from rest_framework.mixins import CreateModelMixin

from apps.meiduo_admin.serializers.users import UserSerializer, UserAddSerializer
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User

"""
class ListAPIView(mixins.ListModelMixin,
                  GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateModelMixin:

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""


# class UserListView(ListAPIView):
#
#     # queryset = User.objects.all()
#     """
#     <QuerySet [
#         <User: itcast>,
#         <User: itcast_01>,
#         <User: itcast_02>,
#         <User: itcast_03>,
#         <User: itcast_04>
#     ]>
#     """
#     def get_queryset(self):
#         keyword = self.request.query_params.get('keyword')
#
#         if keyword:
#             return User.objects.filter(username__contains=keyword)
#
#         return User.objects.all()
#
#     serializer_class = UserSerializer
#
#     pagination_class = PageNum


# 查询所有用户 和   增加新用户 合并
class UserListAPIView(CreateModelMixin, ListAPIView):

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')

        if keyword:
            return User.objects.filter(username__contains=keyword)

        return User.objects.all()

    # serializer_class = UserSerializer
    # serializer_class = UserAddSerializer
    def get_serializer_class(self):

        if self.request.method == 'GET':
            return UserSerializer

        else:
            return UserAddSerializer

    pagination_class = PageNum

    def post(self, request):

        return self.create(request)
