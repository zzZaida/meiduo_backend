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

    # 继承ModelSerializer  可以自己添加字段
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        """
          "username": this.userForm.username,
          "mobile": this.userForm.mobile,
          "password": this.userForm.password,
          "email": this.userForm.email

        """
        # AssertionError: The field 'password2' was declared on serializer UserAddSerializer, but has not been included in the 'fields' option.
        fields = ['username', 'password', 'mobile', 'email', 'password2']

        extra_kwargs = {
            # 只在反序列化(字典-->对象)的时候使用
            # 序列化(对象-->字典)的时候忽略此字段,不在从该模型里获取该字段
            'password': {'write_only': True}
        }

    # AssertionError at /meiduo_admin/users/.validate() should return the validated data
    def validate(self, attrs):

        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('密码不一致')
        return attrs

    # 系统的ModelSerializer.create方法没有设置为密码加密--重写
    # instance = ModelClass._default_manager.create(**validated_data)
    def create(self, validated_data):

        # 模型保存----validated_data{'password2':'1234567890'} 不能入库
        # user = self.model(username=username, email=email, **extra_fields)
        # TypeError: 'password2' is an invalid keyword argument for this function(无效关键字参数)
        del validated_data['password2']
        user = User.objects.create_user(**validated_data)

        return user