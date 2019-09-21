"""
DEV ENVIRONMENT SETTINGS
"""
import os
from .settings_common import *  # IMPORT COMMON SETTINGS

DEBUG = True

ALLOWED_HOSTS = []

# Dev database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tracklistify',
        'USER': os.environ.get('DEV_DB_USER'),
        'PASSWORD': os.environ.get('DEV_DB_PASSWORD'),
        'HOST': os.environ.get('DEV_DB_HOST'),
        'PORT': '5432',
    }
}
