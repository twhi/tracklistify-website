"""
COMMON SETTINGS
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('TRACKLISTIFY_DJANGO_SECRET')

SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'social_django',
    'storages',
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

ROOT_URLCONF = 'tracklistify.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'tracklistify', 'templates')],
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


WSGI_APPLICATION = 'tracklistify.wsgi.application'

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'tracklistify', 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR


AUTHENTICATION_BACKENDS = (
    'social_core.backends.spotify.SpotifyOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_SPOTIFY_KEY = os.environ.get('TRACKLISTIFY_SPOTIFY_KEY')
SOCIAL_AUTH_SPOTIFY_SECRET = os.environ.get('TRACKLISTIFY_SPOTIFY_SECRET')
SOCIAL_AUTH_SPOTIFY_SCOPE = ['user-library-read', 'playlist-modify-public', 'user-read-private']
LOGIN_REDIRECT_URL = ''

##########################################################################
# # security tips from https://reversepython.net/lab/django-web-security-checklist-deployment/
SECURE_HSTS_SECONDS = 18768000  # ~6 months
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True #to avoid transmitting the CSRF cookie over HTTP accidentally.
SESSION_COOKIE_SECURE = True #to avoid transmitting the session cookie over HTTP accidentally.

X_FRAME_OPTIONS = 'DENY'
