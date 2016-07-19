# -*- coding: utf-8 -*-
import os
import sys

# Variables enviroment project

DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)
REPO_DIR = os.path.dirname(WSGI_DIR)
DATA_DIR = os.environ.get('OPENSHIFT_DATA_DIR', BASE_DIR)


# Debugging

DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Admin

ADMINS = (
    ('kleiber', 'kleiberjp@gmail.com'),
)
MANAGERS = ADMINS


# Database
DB_NAME = os.environ['OPENSHIFT_APP_NAME'] if os.environ.has_key('OPENSHIFT_APP_NAME') else ""
DB_USER = os.environ['OPENSHIFT_MYSQL_DB_USERNAME'] if os.environ.has_key('OPENSHIFT_MYSQL_DB_USERNAME') else ""
DB_PASSWD = os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'] if os.environ.has_key('OPENSHIFT_MYSQL_DB_PASSWORD') else ""
DB_HOST = os.environ['OPENSHIFT_MYSQL_DB_HOST'] if os.environ.has_key('OPENSHIFT_MYSQL_DB_HOST') else ""
DB_PORT = os.environ['OPENSHIFT_MYSQL_DB_PORT'] if os.environ.has_key('OPENSHIFT_MYSQL_DB_PORT') else ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


try:
    from local_database import *
except ImportError:
    pass


# I18N & L18N


TIME_ZONE = 'America/Bogota'

LANGUAGE_CODE = 'en-US'

SITE_ID = 1

USE_I18N = True
USE_L10N = True


# Static & Media Files

STATIC_ROOT = os.path.join(os.environ.get('OPENSHIFT_REPO_DIR'), 'wsgi', 'static') if os.environ.has_key('OPENSHIFT_REPO_DIR') else os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Security

SECRETS = "pythonp67+@_t-_-tx55p1(_t#)jt8mb6a*x(oj9hga!j(cr=p61pvxibitgray"
SECRET_KEY = SECRETS

SESSION_COOKIE_DOMAIN = '.bitgray-kperez.rhcloud.com'
SESSION_COOKIE_NAME = 'python-test-bitgray'


# Templates

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'apps.base.context_processor.context_vars',
)


# URl´s apps

ROOT_URLCONF = 'project.urls'


# Deployment

WSGI_APPLICATION = 'project.wsgi.application'


# Application definition


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # admin
    'suit',
    'django.contrib.admin',
    # generic
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    #apps
    'apps.agent',
    'apps.base',
    'apps.contact'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# Host Configuration

from socket import gethostname
WEBPAGE = "http://%s" % os.environ.get('OPENSHIFT_APP_DNS')

ALLOWED_HOSTS = [
    gethostname(),
    os.environ.get('OPENSHIFT_APP_DNS'),
]

PREPEND_WWW = False


# Rest Configuration
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# Admin & Suit

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Bitgray Python Test',
    'HEADER_DATE_FORMAT': 'l, j - F - Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'SEARCH_URL': '',
    # forms
    'SHOW_REQUIRED_ASTERISK': True,
    'CONFIRM_UNSAVED_CHANGES': True,
    # menu
    'MENU_ICONS': {
        'auth': 'icon-lock',
        'djcelery': 'icon-refresh',
        'contacts': 'icon-user',
        'agents': 'icon-tasks',
    },
    'MENU_OPEN_FIRST_CHILD': False,
    'MENU_EXCLUDE': ('auth.group', 'sites',),
    'MENU_ORDER': (
        ('auth', ('user', 'group')),
    ),
    'MENU': (
        'auth',
        'djcelery',
        'agents',
        'contacts',
    ),
    # misc
    'LIST_PER_PAGE': 200
}


# Local settings

try:
    from local_settings import *
except ImportError:
    pass
