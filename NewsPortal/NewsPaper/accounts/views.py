from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.http import HttpResponseRedirect

class PostList(ListView):
    model = Post
    ordering = 'text_of_topic'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_t'] = None

        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostSearch(PostList):
    template_name = 'post_search.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

def post_create(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/posts/')

        form = PostForm()
        return render(request, 'post_create.html', {'form': form})

        def form_valid(self, form):
            if form.is_valid():
                notify_about_new_post_task.delay()
                return redirect('http://127.0.0.1:8000/accounts/')

class PostUpdate(UpdateView):
        form_class = PostForm
        model = Post
        template_name = 'post_edit.html'
        permission_required = ('change_post',)

class PostDelete(DeleteView):
        model = Post
        template_name = 'post_delete.html'
        success_url = reverse_lazy('post_list')
        permission_required = ('post_delete',)



