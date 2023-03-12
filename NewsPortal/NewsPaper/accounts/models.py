from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    rate_of_author = models.IntegerField(default = 0)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def update_rating (self):
        rate_of_post_of_author = Post.objects.filter(author_id = self.pk).aggregate(rating = Sum('rate_of_post'))['rating']
        rate_comments_by_author = Comment.objects.filter(user_id = self.user).aggregate(comment_rating = Sum('rate_comment'))['comment_rating']
        rate_comments_to_posts = Comment.objects.filter(post__author__user = self.user).aggregate(comment_rating = Sum('rate_comment'))['comment_rating']
        self.rate_of_author = rate_of_post_of_author * 3 + rate_comments_by_author + rate_comments_to_posts
        self.save()

sport = 'sp'
politics = 'pt'
educations = 'ed'
weather = 'wt'

CAT = [(sport, 'Спорт'), (politics, 'Политика'), (educations, 'Образование'), (weather, 'Погода')]

class Category(models.Model):
    name_of_category = models.CharField(max_length = 2, choices = CAT, default = politics, unique = True)

news = 'nw'
articles = 'at'

VARS = [(news, 'Новость'), (articles, 'Статья')]
class Post(models.Model):
    var = models.CharField(max_length = 2, choices = VARS, default = news)
    datetime_of_post = models.DateTimeField(auto_now_add = True)
    topic = models.CharField(null = True, max_length=255)
    text_of_topic = models.TextField(null = True)
    rate_of_post = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def previev(self):
        return self.text_of_topic()[:125] + '...' if len(self.text) > 124 else self.text

    def like(self):
        self.rate_of_post += 1
        self.save()

    def dislike(self):
        self.rate_of_post -= 1
        self.save()

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

class Comment(models.Model):
    text_of_comment = models.TextField()
    datetime_of_comment = models.DateTimeField(auto_now_add = True)
    rate_comment = models.IntegerField(default = 0)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def like(self):
        self.rate_comment += 1
        self.save()

    def dislike(self):
        self.rate_comment -= 1
        self.save()

