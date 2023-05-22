from django.contrib import admin
from .models import Post, Category, Author, PostCategory, Comment


def nullfy_rating(modeladmin, request, queryset): # все аргументы уже должны быть вам знакомы, самые нужные из них это request — объект хранящий информацию о запросе и queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(rate_of_post = 0)
nullfy_rating.short_description = 'Обнулить рейтинг'

class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'rate_of_post', 'datetime_of_post')
    list_filer = ('rate_of_post', 'datetime_of_post')
    search_fields = ('topic', 'name_of_category')
    actions = [nullfy_rating]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(PostCategory)
admin.site.register(Comment)
