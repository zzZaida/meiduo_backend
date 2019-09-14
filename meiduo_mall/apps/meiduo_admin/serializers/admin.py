from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['password']

        extra_kwargs = {
            'password': {'write_only': True}
        }



    def create(self, validated_data):

        # User.objects.create_user()

        # 错误写法,系统ModelSerializer可以自己解包
        # user = super().create(**validated_data)
        user = super().create(validated_data)

        # 单独调用加密方法
        user.set_password(validated_data.get('password'))
        user.is_staff = True
        user.save()

        return user

    def update(self, instance, validated_data):
        # 先调用父类,让父类帮我们实现必要的更新的
        super().update(instance, validated_data)

        if validated_data['password']:
            instance.set_password(validated_data.get('password'))
            instance.save()

        return instance