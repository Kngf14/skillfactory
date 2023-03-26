from django_filters import FilterSet, DateFilter, CharFilter, ModelChoiceFilter
from .models import Author, Category, Post
from django import forms

class PostFilter(FilterSet):
    search_title = ModelChoiceFilter(
        field_name='topic',
        label =  'Заголовки',
        queryset=Post.objects.all(),
        empty_label = 'Все',
    )

    search_author = ModelChoiceFilter(
        field_name='author',
        label='Автор',
        queryset=Author.objects.all(),
        empty_label='Все',
    )

    post_date__gt = DateFilter(
        field_name='data',
        label='Дата',
        lookup_expr='date__gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
