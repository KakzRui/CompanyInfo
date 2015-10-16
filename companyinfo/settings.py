"""
Django settings for companyinfo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'clqbsmefee4k(p6jl9b@c0v0!y289i1=t%nnw)9#g%q21%pt(c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'companydetails',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'companyinfo.urls'

WSGI_APPLICATION = 'companyinfo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_RENDERER_CLASSES': ( 
        # 'restapi.renderers.ListWrappingJSONRenderer', 
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', 
    )
    # 'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.OAuth2Authentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
    # )
}


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'CompanyInfo',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'OPTIONS': {
          'autocommit': True,
        },
    }
}

TEMPLATE_DIRS = (
  '/Users/manoj/Documents/companyinfo/templates/',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'file_logging': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/html/logs/company_log.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'db_logging': {
            'level' : 'ERROR',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename': '/var/html/logs/django_db.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/html/logs/django_request.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'soaplib': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/html/logs/soaplib.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['file_logging'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db' : {
            'handlers' : ['db_logging'],
            'level' : 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'soaplib': {
            'handlers': ['soaplib'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}


