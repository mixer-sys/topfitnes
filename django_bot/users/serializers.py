from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from users.models import User, UserInfo


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = (
            'id', 'username', 'password',
            'first_name', 'last_name'
        )


class UserInfoGetSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    class Meta:
        model = UserInfo
        fields = ('id', 'chat', 'age', 'weight', 'height',
                  'sex', 'target', 'user')


class UserInfoPostSerializer(UserInfoGetSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
