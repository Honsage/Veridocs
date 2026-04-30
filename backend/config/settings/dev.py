from .base import *

DEBUG = True

SECRET_KEY = 'django-insecure-(bep1!$g*=mz(j*)l@&@3^w*_v&+k=%=7xonko+bpfh9r45#v3'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}