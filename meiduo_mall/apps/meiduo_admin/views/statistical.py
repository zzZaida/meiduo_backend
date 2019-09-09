

"""
返回所有的用户
1.查询数据库获取数据
2.返回响应

"""

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.goods.models import GoodsVisitCount
from apps.meiduo_admin.serializers.statistical import GoodsVisitCountSerializer
from apps.users.models import User
from datetime import datetime, timedelta


class UserAllCountAPIView(APIView):

    def get(self, request):

        today = datetime.today()

        count = User.objects.all().count()

        return Response({
            'count': count,
            'today': today,

        })

"""
需求分析
    获取当天的注册用户量

大体步骤
    1.获取当天日期
    2.查询数量
    3.返回响应

请求方式和路由
    GET  statistical/day_increment/
"""

from datetime import date
from rest_framework.permissions import IsAuthenticated
class UserDayAddCountAPIView(APIView):

    permission_classes = [IsAuthenticated]


    def get(self, request):
        # 1.获取当天的日期
        # from django.utils import timezone

        today = date.today()
        # 2.查询数量a

        count = User.objects.filter(date_joined__gte=today).count()
        # 3.返回响应
        return Response({
             'count': count,
             'date': today
        })


class UserDayActiveCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 1.获取当天的日期
        # from django.utils import timezone

        today = date.today()
        # 2.查询数量
        count = User.objects.filter(last_login__gte=today).count()
        # 3.返回响应
        return Response({
            'count': count,
            'date': today
        })


"""
需求分析
    获取当天的下单用户量

大体步骤
    1.获取当天日期
    2.查询用户下单的日期是否是今天
    3.返回响应

请求方式和路由
    GET  statistical/day_orders/
"""

class UserDayOrdersCountAPIView(APIView):

    def get(self, request):

        today = date.today()

        count = User.objects.filter(orderinfo__create_time__gte=today).count()

        return Response({
            'count': count
        })

"""
需求分析
    月增用户统计

大体步骤
    1.获取当天日期
    2.获取30天前的日期
    3.遍历
        4. 查询当天的日增
        5. 追加到列表中

请求方式和路由
    GET  statistical/month_increment/
"""
class UserMonthCountAPIView(APIView):

    def get(self, request):
        # 1.获取当天日期
        today = date.today()-timedelta(days=40)
        # 2.获取30天前的日期
        month_start_date = today-timedelta(days=30)

        data = []
        # 3.遍历
        for i in range(30):

            # 查询当天的日增
            start_date = month_start_date + timedelta(days=i)
            end_date = month_start_date + timedelta(days=i+1)

            # 2019-8-10 00:00:00  ~  2019-8-11 00:00:00
            count = User.objects.filter(date_joined__gte=start_date,
                                        date_joined__lte=end_date).count()

            # 追加到列表中
            data.append({
                'date': start_date,
                'count': count
            })

        return Response(data)

"""
需求(做什么功能):
    获取当天的 分类的统计数据

大体步骤(思路,想到什么,就写下来)
    1.获取日期
    2.根据日期进行数据的查询 [GoodsVisitCount,GoodsVisitCount,...]
    3.返回字典/JSON数据
请求方式和路由
GET  statistical/goods_day_views/
"""

class GoodsDayViewCountAPIView(APIView):

    def get(self, request):
        # 1.获取日期
        today = date.today()
        # 2.根据日期进行查询  [GoodsVisitCount, GoodsVisitCount, ...]
        gvcs = GoodsVisitCount.objects.filter(date=today)

        # 进行序列化器的数据转换
        s = GoodsVisitCountSerializer(gvcs, many=True)

        # 3.返回字典/JSON数据
        return Response(s.data)