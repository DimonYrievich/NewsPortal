"""
Django settings for NewsPortal project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rsfh(e)i0ec_em+1uzwxtn#^_e2hu59&mm=bq9=9rrzv-)d(*('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',                     #добавлено и изменено с 'news' на 'news.apps.NewsConfig'
    'django.contrib.sites',                     #добавлено
	'django.contrib.flatpages',                 #добавлено
#    'fpages',                                   #добавлено
    'django_filters',                           #добавлено
    'sign',                                     #добавлено
    'allauth',                                  #добавлено
    'allauth.account',                          #добавлено
    'allauth.socialaccount',                    #добавлено
    # ... include the providers you want to enable (в нашем случае google):
    'allauth.socialaccount.providers.google',   #добавлено
    "django_apscheduler",                       #добавлено (при создании команды "python manage.py runapscheduler")
]

SITE_ID = 1                                     #добавлено

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'    #добавлено
]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'                          #Можно указать 'mandatory' вместо 'none' для верификации при регистрации

ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}    # для создания групп пользователей


LOGIN_URL = '/sign/login/'                     # для входа в систему
LOGIN_REDIRECT_URL = '/'                       # cтраница авторизованного пользователя

WSGI_APPLICATION = 'NewsPortal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


SITE_URL = 'http://127.0.0.1:8000'                  #Локальный хост

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'dmitry.glumin'
EMAIL_HOST_PASSWORD = '322223'                      #пароль изменен, чтобы не палиться
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'dmitry.glumin@yandex.ru'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"       #указываем формат, когда будет производиться рассылка
APSCHEDULER_RUN_NOW_TIMEOUT = 25                    #указываем время, за которое должна обрабатываться функция (в секундах)


#Если используется Redis Labs, то переменные CELERY_BROKER_URL и CELERY_RESULT_BACKEND должны строиться по шаблону:
#redis://логин:пароль@endpoint:port (всё берется из конфигурации созданной новой базы данных в redis)
CELERY_BROKER_URL = 'redis://:ZAYAGreQx6DfLRmMVjMze96VIPo8pKwp@redis-12964.c264.ap-south-1-1.ec2.cloud.redislabs.com:12964'
CELERY_RESULT_BACKEND = 'redis://:ZAYAGreQx6DfLRmMVjMze96VIPo8pKwp@redis-12964.c264.ap-south-1-1.ec2.cloud.redislabs.com:12964'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

