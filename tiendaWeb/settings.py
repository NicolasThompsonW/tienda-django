"""
Django settings for tiendaWeb project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""


from django.contrib.messages import constants as mensajes_de_error
from pathlib import Path
import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y*ni-)u8bv6cpn=-*^rrt72+wa_9hxf5p!7o01ugxunb-mbt&r"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',
                 'tienda-django-production.up.railway.app']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",



    'tiendaApp',
    'servicios',
    'blog',
    'contacto',
    'tienda',
    'carro',
    "autenticacion",
    "crispy_forms",
    'pedidos'
]

MIDDLEWARE = [


    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tiendaWeb.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "carro.context_processor.importe_total_carro"
            ],
        },
    },
]

WSGI_APPLICATION = "tiendaWeb.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
""" 
una manera de conectarse 

import dj_database_url
DATABASES = {'default': dj_database_url.config(
    default='postgresql://postgres:UGtctL7dlGSxlJqsc2um@containers-us-west-162.railway.app:6362/railway', engine='django.db.backends.postgresql')}
 """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'UGtctL7dlGSxlJqsc2um',
        'HOST': 'containers-us-west-162.railway.app',
        'PORT': '6362',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "es-ar"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


#STATIC_URL = "static/"
#MEDIA_URL = "media/"
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'staticfiles/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Configuracion de email

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# clave de google
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


CRISPY_TEMPLATE_PACK = "bootstrap4"

MESSAGES_TAGS = {
    mensajes_de_error.DEBUG: 'debug',
    mensajes_de_error.INFO: 'info',
    mensajes_de_error.SUCCESS: 'seccess',
    mensajes_de_error.WARNING: 'warnig',
    mensajes_de_error.ERROR: 'danger',
}
MIME_TYPE = 'application/javascript'
