from rest_framework import serializers

from apps.users.models import User

# 用户的展示
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'mobile', 'email']


# 用户的新增
# widget---->弹出框
"""
前端收集数据(dict)--axios.post请求---后端接收数据(dict--object)--验证数据--数据入库--返回响应

CreateModelMixin(serializer.save()触发--->ModelSerializer.create())

"""
class UserAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        """
          "username": this.userForm.username,
          "mobile": this.userForm.mobile,
          "password": this.userForm.password,
          "email": this.userForm.email

        """

        fields = ['username', 'password', 'mobile', 'email']

        extra_kwargs = {
            # 只在反序列化(字典-->对象)的时候使用
            # 序列化(对象-->字典)的时候忽略此字段,不在从该模型里获取该字段
            'password': {'write_only': True}
        }


    # 系统的ModelSerializer.create方法没有设置为密码加密--重写
    # instance = ModelClass._default_manager.create(**validated_data)
    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user