import os                               # Импортируем библиотеку для взаимодействия с операционной системой и
from celery import Celery               # саму библиотеку Celery
from celery.schedules import crontab    # Импортируем crontab, который позволяет задавать расписание(периодичность), ориентируясь на точное время


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')  # Cвязываем настройки Django с настройками Celery через переменную окружения

app = Celery('NewsPortal')                                              # Cоздаём экземпляр приложения Celery и устанавливаем для него файл конфигурации. Мы также указываем пространство имён, чтобы Celery сам
app.config_from_object('django.conf:settings', namespace='CELERY')      # находил все необходимые настройки в общем конфигурационном файле settings.py. Он их будет искать по шаблону «CELERY_***».

# Указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта
app.autodiscover_tasks()

# Реализуем еженедельную рассылку с последними новостями (каждый понедельник в 8:00 утра)
app.conf.beat_schedule = {
     'when_week': {
         'task': 'news.tasks.notify_weekly',
         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
     },
}

# Реализуем рассылку уведомлений подписчикам, которая будет выполняться при создании нового поста
# app.conf.beat_schedule = {'when_creating_post': {'task': 'news.tasks.notify_about_new_post', 'schedule': 30}} - удалил, т.к. такую рассылку делали в модуле D9 при подписке на конкретную категорию поста



