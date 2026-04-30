from .base import *

DEBUG = False

# Production domain must be specified there
ALLOWED_HOSTS = ['sedas.ru']

# Remove db credentials in production 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sedas',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}