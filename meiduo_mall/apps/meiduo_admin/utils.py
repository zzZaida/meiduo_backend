from collections import OrderedDict

from rest_framework.response import Response


def jwt_response_payload_handler(token, user=None, request=None):
    # token jwt生成的token
    # user 我们的登录用户信息
    # request 请求
    return{
        'token': token,
        'username': user.username,
        'id': user.id
    }


from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PageNum(PageNumberPagination):
    # 默认返回是5条数据
    page_size = 5
    # 前端发送请求来获取指定的页数
    page_size_query_param = 'pagesize'
    # 约束返回的最大条数
    max_page_size = 20

    """
    系统分页返回数据:
{
  "count": 7,
  "next": "http://127.0.0.1:8000/meiduo_admin/users/?pagesize=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "username": "itcast",
      "mobile": "18310820688",
      "email": "qi_rui_hua@163.com"
    },
    {
      "id": 2,
      "username": "itheima",
      "mobile": "18310820686",
      "email": ""
    },
    {
      "id": 3,
      "username": "itcast_01",
      "mobile": "18310820687",
      "email": ""
    },
    {
      "id": 4,
      "username": "itcast_02",
      "mobile": "18310820685",
      "email": "qiruihua@itcast.cn"
    },
    {
      "id": 5,
      "username": "itcast_03",
      "mobile": "13812345678",
      "email": "qiruihua@itcast.cn"
    }
  ]
}
    """

    """
    需求:
     {
        "count": "用户总量",
        "lists": [
            {
                "id": "用户id",
                "username": "用户名",
                "mobile": "手机号",
                "email": "邮箱"
            },
            ...
        ],
        "page": "页码",
        "pages": "总页数",
        "pagesize": "页容量"
      }
    """

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            # self.page = paginator.page(page_number)
            ('count', self.page.paginator.count),      # 总数量
            ('page', self.page.number),                # 当前的页码
            ('pages', self.page.paginator.num_pages),  # 总页数
            ('pagesize', self.page_size),              # 每页多少条数据
            ('lists', data)                            # 数据
        ]))
