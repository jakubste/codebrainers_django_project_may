
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    View,
    ListView,
)

from .models import Post

# def hello_world(request):
#     print(request)
#     # return HttpResponse('<b>Hello world!</b>')
#     return render(request, 'posts/index.html')

# class HelloWorldView(View):
#     def get(self, request, *args, **kwargs):
#           return render(request, 'posts/index.html')

class HelloWorldView(TemplateView):
    template_name = 'base.html'


class PostList(ListView):
    template_name = 'posts/list.html'
    # queryset = Post.objects.filter(published=True)
    model = Post

    extra_context = {
        'title': 'Wpisy',
    }
