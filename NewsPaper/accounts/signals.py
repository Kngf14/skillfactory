from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from accounts.models import PostCategory

def send_notifications(previev, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': previev,
            'link': f'{settings.SITE_URL}/posts/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject = title,
        body = ' ',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = subscribers,
    )

    msg.attach.alternative(html_content, 'text/html')
    msg.send()

@receiver(m2m_changed, sender = PostCategory)
def notify_about_news_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)
