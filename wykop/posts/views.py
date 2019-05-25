
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    View,
    ListView,
    DetailView,
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


class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        return data
