from rest_framework.serializers import ModelSerializer
from .models import Post,User


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post


class UserSerializer(ModelSerializer):
    class Meta:
        model = User

