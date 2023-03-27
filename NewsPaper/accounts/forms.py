from django import forms
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