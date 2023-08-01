from django.shortcuts import render
from .models import User, Post
from rest_framework import status, viewsets, permissions
from .serializers import PostSerializer, UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True)
    def user_posts(self, request, pk=None):
        posts = Post.objects.filter(user=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
# Create your views here.
