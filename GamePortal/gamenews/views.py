from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

from .models import Callboard, Category, Reply

class CallList(ListView):
    model = Callboard
    ordering = 'text_of_call'
    template_name = 'callboard/call_list.html'
    context_object_name = 'calls'
    paginate_by = 10

def call_detail_view(request, pk):
    template_name = 'callboard/call_detail.html'
    callb = get_object_or_404(Callboard, id=pk)
    replies = adv.replies.filter(approved=True)
    new_reply = None
    if request.method == 'POST':
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.callb = callb
            new_reply.user = request.user
            new_reply.save()
            reply_add_notification.delay(new_reply.pk)
    else:
        reply_form = ReplyForm()

    context = {
        'callb': callb,
        'replies': replies,
        'new_reply': new_reply,
        'reply_form': reply_form
    }

    return render(request, template_name, context)

class CallCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    form_class = CallForm
    model = Callboard
    template_name = 'callboard/call_create.html'
    permission_required = ('call.add_callboard',)

    def form_valid(self, form):
        if form.is_valid():
            notify_about_new_call_task.delay()
            return redirect('http://127.0.0.1:8000/callboard')

class CallUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    form_class = CallForm
    model = Callboard
    template_name = 'callboard/call_edit.html'
    permission_required = ('call.edit_callboard',)

class CallDelete(DeleteView):
    model = Callboard
    template_name = 'callboard/call_delete.html'
    success_url = reverse_lazy('call_list')
    permission_required = ('call_delete',)

class CategoryListView(ListView):
    template_name = 'callboard/category_list.html'
    context_object_name = 'category_call_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Callboard.objects.filter(category=self.category).order_by()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context
