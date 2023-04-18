from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .tasks import hello

class HelloView(View):
    def get(self, request):
        hello.delay()
        return HttpResponse('Hello!')

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
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
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

class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    permission_required = ('posts.add_post',)

    def form_valid(self, form):
        if form.is_valid():
            notify_about_new_post_task.delay()
            return redirect('http://127.0.0.1:8000/posts')

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
        form_class = PostForm
        model = Post
        template_name = 'post_edit.html'
        permission_required = ('post_edit',)

class PostDelete(DeleteView):
        model = Post
        template_name = 'post_delete.html'
        success_url = reverse_lazy('post_list')
        permission_required = ('post_delete',)

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id = self.kwargs['pk'])
        queryset = Post.objects.filter(category = self.category).order_by()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id = pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку категории'
    return render(request, 'subscribe.html', {'category': category, 'message': message})

