from rest_framework import routers
from django.urls import path, include

from wykop.posts.views import PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
