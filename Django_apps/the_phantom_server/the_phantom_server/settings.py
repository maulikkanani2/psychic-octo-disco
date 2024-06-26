"""
Django settings for the_phantom_server project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# settings.py


TRANS_API_URL = config('TRANS_API_URL')
#ENDPOINT2_URL = config('ENDPOINT2_URL')
# Fetch more as needed...
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','157.245.87.41','localhost', '*']


# Application definition

INSTALLED_APPS = [
    'django_descope',
    'django.contrib.gis',
    'bi_app.apps.BiAppConfig',
    'land_app.apps.LandAppConfig',
    'finance_app.apps.FinanceAppConfig',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_pivot',
    'debug_toolbar',
    'django_filters',
    'authentication'
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django_descope.middleware.DescopeMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]



INTERNAL_IPS = [
    # ...
    '127.0.0.1',  # Add your development machine's IP address
]


ROOT_URLCONF = 'the_phantom_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'the_phantom_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('POSTGRES_ENGINE'),
        'NAME': config('DEFAULT_DB_NAME'),
        'USER': config('DEFAULT_DB_USER'),
        'PASSWORD': config('DEFAULT_DB_PASSWORD'),
        'HOST': config('DEFAULT_DB_HOST'),
        'PORT': config('DEFAULT_DB_PORT'),
        'TEST': {
            'MIRROR': 'default',
        },
    },
    'secondary': {
        'ENGINE': config('POSTGRES_ENGINE'),
        'NAME': config('SECONDARY_DB_NAME'),
        'USER': config('SECONDARY_DB_USER'),
        'PASSWORD': config('SECONDARY_DB_PASSWORD'),
        'HOST': config('SECONDARY_DB_HOST'),
        'PORT': config('SECONDARY_DB_PORT'),
        'TEST': {
            'MIRROR': 'secondary',
        },
    },
    'third_db': {
        'ENGINE': config('POSTGRES_ENGINE'),
        'NAME': config('THIRD_DB_NAME'),
        'USER': config('THIRD_DB_USER'),
        'PASSWORD': config('THIRD_DB_PASSWORD'),
        'HOST': config('THIRD_DB_HOST'),
        'PORT': config('THIRD_DB_PORT'),
        'TEST': {
            'MIRROR': 'third_db',
        },
    },

}


DATABASE_ROUTERS = ['land_app.routers.Gis_Router','finance_app.routers.FinanceRouter'] #router order is important

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT= os.path.join(BASE_DIR, "media")
MEDIA_URL="media/"
STATICFILES_DIRS = [
    BASE_DIR+'/static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MODAM_API_KEY = config('API_KEY', "")
SIX_FAB_URL = config('SIX_FAB_URL')
LOGIN_URL = 'login'

#Dscope Configuretion
# https://docs.descope.com/?_gl=1*16st2af*_gcl_au*MzE4MDE2ODA0LjE3MDgzMjAzMDU.
DESCOPE_PROJECT_ID = config('DESCOPE_PROJECT_ID', "P2cZXCbVTo17pW6JtDf23T2hlMYp")
DESCOPE_IS_STAFF_ROLE = config('DESCOPE_IS_STAFF_ROLE', "is_staff")
DESCOPE_IS_SUPERUSER_ROLE = config('DESCOPE_IS_SUPERUSER_ROLE', "is_superuser")
DESCOPE_IS_FINANCE_ROLE = config('DESCOPE_IS_FINANCE_ROLE', "is_finance")
DESCOPE_IS_STORE_DATA_ROLE = config('DESCOPE_IS_STORE_DATA_ROLE', "is_store_data")

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#         "file": {
#             "class": "logging.FileHandler",
#             "filename": "event.log",  # Specify the path to your log file
#         },
#     },
#     "root": {
#         "handlers": ["console", "file"],
#         "level": "DEBUG",
#     },
# }

#Configuretion Celery
BROKER_URL = config('REDIS_BROKER_URL', '')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_TRACK_STARTED = True
CELERY_BROKER_URL = config('REDIS_BROKER_URL', '')
CELERY_RESULT_BACKEND = config('REDIS_BROKER_URL', '')
CELERY_TIMEZONE = TIME_ZONE

#Google Configuretion
SCOPES = config('SCOPES', "")
GOOGLE_DRIVE_CLIENT_ID = config('GOOGLE_DRIVE_CLIENT_ID', "")
GOOGLE_DRIVE_CLIENT_SECRET = config('GOOGLE_DRIVE_CLIENT_SECRET', "")
GOOGLE_DRIVE_REDIRECT_URI = config('GOOGLE_DRIVE_REDIRECT_URI', "")
GOOGLE_DRIVE_AUTH_URL = config('GOOGLE_DRIVE_AUTH_URL', "")
GOOGLE_DRIVE_TOKEN_URL = config('GOOGLE_DRIVE_TOKEN_URL', "")
GOOGLE_DRIVE_CLIENT_SECRET_JSON_FILE = config('GOOGLE_DRIVE_CLIENT_SECRET_JSON_FILE',"")
GOOGLE_DRIVE_FOLDER = config('GOOGLE_DRIVE_FOLDER', "")