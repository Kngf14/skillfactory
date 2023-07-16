from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError
from .models import Callboard, Category, Reply

class CallbForm(forms.ModelForm):
   class Meta:
       model = Callboard
       fields = [
           'headline',
           'text',
           'category'
       ]

   def clean(self):
       cleaned_data = super().clean()
       headline = cleaned_data.get('headline')
       text = cleaned_data.get('text')
       if text == headline:
           raise ValidationError('Текст не должен быть идентичен заголовку')
       return cleaned_data

   headline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), min_length=20, max_length=128,
                              label='Заголовок')
   category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     empty_label='Выберите категорию', label='Категория')


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name = 'common')
        basic_group.user_set.add(user)
        return