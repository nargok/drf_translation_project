from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from drf_translation.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
  """
  ユーザの参照や編集をさせるAPIのエンドポイント
  """
  queryset = User.objects.all().order_by('-date_joined')
  serialzer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  """
  グループの参照や編集をさせるAPIのエンドポイント
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer