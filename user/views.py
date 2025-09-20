from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user.serializers import ManageUserSerializer, UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = ()


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = ManageUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
