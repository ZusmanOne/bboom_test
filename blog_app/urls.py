from django.urls import path, include
from .views import get_users, get_user_posts, delete_post, create_post
from .api import PostList, PostDetail, UserList, UserDetail, PostUserList, api_root


urlpatterns = [

    path('api/', api_root),
    path('', get_users, name='get-users'),
    path('users/<int:pk>/', get_user_posts, name='get-user-posts'),
    path('post/delete/<int:pk>/', delete_post, name='post-delete'),
    path('post/add/', create_post, name='create-post'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/posts/', PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/posts/<str:username>/', PostUserList.as_view(), name='user_posts'),
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),

]
