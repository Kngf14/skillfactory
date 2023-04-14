from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'topic',
           'text_of_topic',
           'category',
           'var'
       ]

   def clean(self):
       cleaned_data = super().clean()
       topic = cleaned_data.get('topic')
       text_of_topic = cleaned_data.get('text_of_topic')
       if text_of_topic == topic:
           raise ValidationError('Текст не должен быть идентичен заголовку')
       return cleaned_data

class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name = 'common')
        basic_group.user_set.add(user)
        return