"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import platform
from configparser import RawConfigParser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Loading settings.ini file with PostgreSQL database credentials
config = RawConfigParser()
config.read(BASE_DIR + '/settings.ini')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*n3hoks6ece)zj)w95aoh=vzvf(2%e!uzws@s_28w60top2lwh'

# Google Maps API Config
API_KEY = config.get('googleMapsConf', 'API_KEY')
defaultLat = config.get('googleMapsConf', 'defaultLat')
defaultLng = config.get('googleMapsConf', 'defaultLng')

# GEOSGeometry Config
max_distance = config.get('GEOSGeometryConf', 'max_distance')

# Amazon S3 Config
S3_ACCESS_KEY = config.get('amazonS3Conf', 'S3_ACCESS_KEY')
S3_SECRET_KEY = config.get('amazonS3Conf', 'S3_SECRET_KEY')
s3_bucket_name = config.get('amazonS3Conf', 's3_bucket_name')

# Fond awesome Config
try:
    FONT_AWESOME_KEY=config.get('font-awesomeConf', 'KEY')
except Exception as e:
    FONT_AWESOME_KEY=''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'api',
    'frontend',
    'rest_framework',
    'django.contrib.gis'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('postgresdbConf', 'DB_ENGINE'),
        'NAME': config.get('postgresdbConf', 'DB_NAME'),
        'USER': config.get('postgresdbConf', 'DB_USER'),
        'PASSWORD': config.get('postgresdbConf', 'DB_PASS'),
        'HOST': config.get('postgresdbConf', 'DB_HOST'),
        'PORT': config.get('postgresdbConf', 'DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

# Custom User
# https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user

AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
if(platform.system() == 'Windows'):
    STATICFILES_DIRS = (BASE_DIR + '/static'),
elif(platform.system() == 'Linux'):
    STATICFILES_DIRS = (BASE_DIR + STATIC_URL),

###################################################################
##### REST_FRAMEWORK
###################################################################

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_DIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

###################################################################
##### LOGGING CONFIG 
###################################################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'standard': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/default.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'debug_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/debug.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'warning_file': {
            'level':'WARNING',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/warning.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'info_file': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/info.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'error_file': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/error.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'emails': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR + '/logs/emails.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'debug_logger': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'info_logger': {
            'handlers': ['info_file'],
            'level': 'INFO',
            'propagate': True
        },
        'error_logger': {
            'handlers': ['error_file'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.request': {
            'handlers': ['default', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'emails': {
            'handlers': ['emails'],
            'level': 'DEBUG',
            'propagate': True
        },

    }
}
