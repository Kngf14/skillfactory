from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category
from datetime import datetime

class PostsList(ListView):
    model = Post
    ordering = 'text_of_topic'
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_t'] = None


        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

# Create your views here.
