from rest_framework import viewsets

from users.models import UserInfo
from users.serializers import UserInfoGetSerializer, UserInfoPostSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    lookup_field = 'chat'

    def get_serializer_class(self):
        if self.action == 'create':
            return UserInfoPostSerializer
        return UserInfoGetSerializer
