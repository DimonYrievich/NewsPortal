# Cогласно рекомендациям из документации к Celery, мы должны добавить следующие строки в файл __init__.py (Это для настройки пакета "Celery")

from .celery import app as celery_app

__all__ = ('celery_app',)