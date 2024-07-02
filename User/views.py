from rest_framework import generics
from .models import User
from .serializers import UserSer
from rest_framework.permissions import IsAuthenticated


class Users(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSer


class UserOther(generics.ListAPIView):
    serializer_class = UserSer
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk'])