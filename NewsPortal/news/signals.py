                                                # РАССЫЛКА

from django.db.models.signals import m2m_changed        #импортируем нужный сигнал (m2m_changed)
from django.dispatch import receiver                    #импортируем нужный декоратор
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from .models import PostCategory


def send_notifications(preview, pk, title, subscribers):                 #функция отправки сообщений
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,                                             #передаем превью
            'link': f'{settings.SITE_URL}/cheburashka/{pk}'              #передаем полную ссылку на статью
        }
    )

    msg = EmailMultiAlternatives(
        subject = title,
        body = '',
        from_email = settings.DEFAULT_FROM_EMAIL,                       #от кого
        to = subscribers,                                               #кому
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()

# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(m2m_changed, sender = PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers: list[str] = []                                     #список подписчиков
        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]                #список адресов почт подписчиков

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)