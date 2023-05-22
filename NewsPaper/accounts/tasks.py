from celery import shared_task
import datetime
import time
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from NewsPaper import settings
from NewsPaper.settings import SITE_URL
from accounts.models import Post, Category

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

@shared_task
def send_notify(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_context)
    msg.send()

@shared_task()
def weekly_notify():
    categories = Category.objects.all()
    for category in categories:
        subscribers = category.subscribers.all()
        posts = Post.objects.filter(category=category, time_date__gte=datetime.datetime.now() - datetime.timedelta(days=7))
        if posts.exists():
            subject = f'Ознакомьтесь с новыми статьями {category.get_category_name_display()}'
            html_context = render_to_string(
                'weekly_notify.html',
                {
                    'category': category,
                    'posts': posts,
                    'link': Site.objects.get_current().domain,
                }
            )
            msg = EmailMultiAlternatives(
                subject=subject,
                body='',
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[s.email for s in subscribers],
            )
            msg.attach_alternative(html_context)
            msg.send()