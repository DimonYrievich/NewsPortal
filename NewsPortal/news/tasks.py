                                                        #ЗАДАЧИ#

from celery import shared_task
import datetime
from .models import Post, Category, PostCategory
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task
def notify_weekly():
    today = datetime.datetime.now()
    last_week = today-datetime.timedelta(days=7)
    posts = Post.objects.filter(posting_time__gte=last_week)
    print(posts)
    categories = set(posts.values_list('category__name_category', flat=True))
    print(categories)
    subscribers = set(Category.objects.filter(name_category__in=categories).values_list("subscribers__email", flat=True))
    print(subscribers)
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    print(html_content)
    msg = EmailMultiAlternatives(
        subject="Не забудь посмотреть!",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,                 #от кого
        to=subscribers,                                         #кому
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
