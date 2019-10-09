# Django settings for project.
import os
import json
from urllib.parse import urlparse

from .utils import path, BASE, PROJECT, config

from config.settings import AUTH_USER_MODEL, INSTALLED_APPS

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

url = urlparse(config.get("general", "database"))
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.' + url.scheme,
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port    }
}

if url.scheme == "mysql":
    DATABASES['default']['OPTIONS'] = { 'init_command': 'SET storage_engine=INNODB;' }
elif url.scheme == 'postgres':
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
elif url.scheme == "sqlite3":
    DATABASES['default']['NAME'] = path(DATABASES['default']['NAME'])

DEBUG = config.get("general", "debug") == "true"

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = config.get("security", "hosts").split(",")

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = path(config.get('path', 'media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = config.get('url', 'media')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = path(config.get('path', 'static'))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = config.get('url', 'static')

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
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.get("security", "secret")

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

if config.get("auth", "enabled") == "true":
    TEMPLATES[0]["OPTIONS"]["context_processors"].append('django.contrib.auth.context_processors.auth')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

if config.get("cache", "cachesite") == "true":
    MIDDLEWARE.append('django.middleware.cache.UpdateCacheMiddleware')

MIDDLEWARE.extend([
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
])

if config.get("auth", "enabled") == "true":
    MIDDLEWARE.extend([
        'django.contrib.auth.middleware.AuthenticationMiddleware',
])

MIDDLEWARE.extend([
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
])

if config.get("cache", "cachesite") == "true":
    MIDDLEWARE.append('django.middleware.cache.FetchFromCacheMiddleware')

ROOT_URLCONF = "%s.urls" % BASE

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "%s.wsgi.application" % BASE

INSTALLED_APPS.insert(0, 'django.contrib.staticfiles')
INSTALLED_APPS.insert(0, 'django.contrib.messages')
INSTALLED_APPS.insert(0, 'django.contrib.sessions')

if config.get("auth", "enabled") == "true":
    INSTALLED_APPS.extend(['django.contrib.auth', 'django.contrib.contenttypes'])

if config.get("admin", "enabled") == "true":
    INSTALLED_APPS.append('django.contrib.admin')

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

if config.get("cache", "enabled") == "true":
    CACHES = {
        'default': {
            'BACKEND': "django.core.cache.backends.%s" % config.get("cache", "backend"),
            'LOCATION': config.get("cache", "location"),
            'TIMEOUT': config.get("cache", "timeout"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
