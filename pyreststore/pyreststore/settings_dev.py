# -*- coding: utf-8; mode: Python; -*-
'''
Development Django settings for pyreststore project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
'''

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j&$o0j6q8!mj2z(4e^tdglp+fq&nwzw!qv@niwe$a5f!mswec*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_nose',
    'test_pep8',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'bckt',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pyreststore.urls'

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

WSGI_APPLICATION = 'pyreststore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

REST_FRAMEWORK = {
    # Page size
    # defaults to 10 items, may be modified by the client in the request.
    # Examples: GET /bckt/?page_size=2
    #           GET /bckt/?page=1&page_size=2
    #           GET /bckt/?page=2&page_size=2
    'PAGINATE_BY': 10,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100000,
    # Use djangorestframework-jwt
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# test_pep8 (usage: 'python manage.py test -v 2 test_pep8')
TEST_PEP8_DIRS = [BASE_DIR, ]
TEST_PEP8_EXCLUDE = ['migrations', ]  # Exclude this paths from tests

# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-package=pyreststore,bckt',
    '--cover-inclusive',
    '--cover-html',
    '--cover-html-dir=coverage-html',
]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ' '.join(['%(levelname)s',
                                '%(asctime)s',
                                '%(module)s',
                                '%(process)d',
                                '%(thread)d',
                                '%(message)s'])
        },
        'verbose debug': {
            'format': ' '.join(['%(levelname)s',
                                '%(asctime)s',
                                '%(module)s',
                                '%(name)s',
                                '%(process)d',
                                '%(thread)d',
                                '%(message)s'])
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose debug',
            'filename': 'pyreststore-debug.log',
        },
    },
    'loggers': {
        'tests.test_bckt.test_bckt_views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'tests': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'bckt': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'pyreststore': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
