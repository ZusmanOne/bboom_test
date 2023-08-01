from rest_framework import serializers
from .models import Post, User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='posts-detail', read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='users-detail', lookup_field='pk')

    class Meta:
        model = User
        fields = ['url', 'id', 'email', 'username', 'posts']

