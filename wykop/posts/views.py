from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.aggregates import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)

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
    # queryset = Post.objects.filter(published=True).order_by('-created')
    model = Post
    ordering = '-created'
    paginate_by = 3

    extra_context = {
        'title': 'Wpisy',
    }


class TopPostsList(PostList):
    queryset = Post.objects.annotate(score=Sum('votes__value')).order_by('-score')
    ordering = ''

    extra_context = {
        'title': 'Najlepsze wpisy',
    }

class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = self.object.title
        return data


class PostCreate(LoginRequiredMixin, CreateView):
    template_name = 'posts/create.html'
    model = Post
    fields = ['title', 'text', 'image']

    extra_context = {
        'title': 'Dodawanie wpisu',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['title', 'text', 'image']

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['title'] = 'Edycja ' + self.object.title
        return data


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy('posts:list')

    def test_func(self):
        obj = self.get_object()
        return (
            (self.request.user == obj.author) and
            (timezone.now() - obj.created < timedelta(0, 15*60))
        )
