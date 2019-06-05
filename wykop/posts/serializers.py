from rest_framework import serializers

from wykop.accounts.serializers import UserSerializer
from wykop.posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created', 'image', 'video', 'author')
        read_only_fields = ('author', )

    author = UserSerializer(read_only=True)
