from django.urls import path,include
from .views import PostViewSet,UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/blog', PostViewSet, basename='posts')
router.register('api/users', UserViewSet, basename='users')
urlpatterns = router.urls


urlpatterns += [

    path('api/auth/', include('rest_framework.urls')),

]
