import datetime
from celery import shared_task
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .models import Callboard, Category, Reply
import time
from django.contrib.sites.models import Site
from GamePortal import settings
from GamePortal.settings import SITE_URL


def subscribers_send_mails(pk, headline, subscribers_emails):
    html_context = render_to_string(
        'mail/adv_add_email.html',
        {
            'link': f'{settings.SITE_URL}/callb/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=headline,
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = subscribers_emails,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send(fail_silently = False)

def callb_author_send_mail(pk, email):
    html_context = render_to_string(
        'mail/reply_add_email.html',
        {
            'link': f'{settings.SITE_URL}/callb/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject = 'Новый отклик',
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = email,
    )
    msg.attach_alternative(html_context, 'text/html')
    msg.send(fail_silently = False)

def reply_author_send_mail(pk, email):
    html_context = render_to_string(
        'mail/reply_approve_email.html',
        {
            'link': f'{settings.SITE_URL}/callb/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject = 'Принято',
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,
        to = email,
    )

    msg.attach_alternative(html_context, 'text/html')
    msg.send(fail_silently = False)

@shared_task
def my_job():
    today = datetime.datetime.now()
    week_ago = today - datetime.timedelta(days = 7)
    callb = Callboard.objects.filter(created_at__gte = week_ago)
    categories = set(ads.values_list('category__name', flat = True))
    subscribers_emails = set(Category.objects.filter(name__in = categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'mail/weekly_callb.html',
        {
            'link': settings.SITE_URL,
            'callb': ads
        }
    )