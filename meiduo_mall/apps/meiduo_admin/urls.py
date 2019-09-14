from django.conf.urls import url
from . import views

# 导入jwt视图
from rest_framework_jwt.views import obtain_jwt_token

from .views import statistical
from .views import users
from .views import image
from .views import sku
from .views import spu
from .views import order
from .views import permission


urlpatterns = [

    url(r'^authorizations/$', obtain_jwt_token),

    # http://127.0.0.1:8000/meiduo_admin/authorizations/
    # url(r'^authorizations/$', views.AdminLoginAPIView.as_view())

    ##########################statistical#########################
    url(r'^statistical/total_count/$', statistical.UserAllCountAPIView.as_view()),
    url(r'^statistical/day_increment/$', statistical.UserDayAddCountAPIView.as_view()),
    url(r'^statistical/day_active/$', statistical.UserDayActiveCountAPIView.as_view()),
    url(r'^statistical/day_orders/$', statistical.UserDayOrdersCountAPIView.as_view()),
    url(r'^statistical/month_increment/$', statistical.UserMonthCountAPIView.as_view()),
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayViewCountAPIView.as_view()),


    ##########################User 相关#########################
    url(r'^users/$', users.UserListAPIView.as_view()),


    ###########################image 相关##########################
    url(r'^skus/simple/$', image.SimpleSKUListAPIView.as_view()),


    ############################sku相关####################################
    url(r'^skus/categories/$', sku.ThreeCategoryListAPIView.as_view()),
    url(r'^goods/simple/$', sku.SPUListAPIView.as_view()),
    # 规格信息获取
    url(r'^goods/(?P<pk>\d+)/specs/$', sku.SPUSpecsAPIView.as_view()),


    ##########################权限相关#########################
    url(r'^permission/content_types/$', permission.ContentTypeAPIView.as_view()),

]


# 图片管理的url
from rest_framework.routers import DefaultRouter

# 创建router实例对象
router = DefaultRouter()
# 注册路由
router.register(r'skus/images', image.ImageModelViewSet, basename='images')
# 将路由追加到urlpatterns
urlpatterns += router.urls


#####################SKU路由###########################
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'skus', sku.SKUModelViewSet, basename='skus')

urlpatterns += router.urls


#####################Order路由###########################
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'orders', order.OrderModelViewSet, basename='orders')

urlpatterns += router.urls


#########################SPU路由################################
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
#
# router.register(r'goods', spu.SPUGoodsPAIView.as_view, basename='goods')
#
# urlpatterns += router.urls



#####################权限路由###########################
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'permission/perms', permission.PermissionModelViewSet, basename='permission')

urlpatterns += router.urls