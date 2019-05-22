from django.contrib import admin

from wykop.posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author')


admin.site.register(Post, PostAdmin)
