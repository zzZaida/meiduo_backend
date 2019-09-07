from django.conf.urls import url
from . import views


urlpatterns = [

    # http://127.0.0.1:8000/meiduo_admin/authorizations/
    url(r'^authorizations/$', views.AdminLoginAPIView.as_view())
]