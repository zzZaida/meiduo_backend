from django.conf.urls import url
from . import views

# 导入jwt视图
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [

    url(r'^authorizations/', obtain_jwt_token),

    # http://127.0.0.1:8000/meiduo_admin/authorizations/
    # url(r'^authorizations/$', views.AdminLoginAPIView.as_view())

]