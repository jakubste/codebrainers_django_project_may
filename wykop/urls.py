"""wykop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from wykop.posts.views import (
    HelloWorldView,
    PostList,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wykop.accounts.urls')),
    # path('', hello_world),
    path('', HelloWorldView.as_view()),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/new', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('post/<int:pk>/edit', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post-delete'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
