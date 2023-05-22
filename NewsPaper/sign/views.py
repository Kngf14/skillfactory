from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

    success_url = 'http://127.0.0.1:8000/posts/'

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = 'http://127.0.0.1:8000/posts/'

@login_required
def become_author(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/posts/search/')
