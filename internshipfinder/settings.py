# Django settingsfor internshipfinder:
# tells django how project works
# stores important info (apps, settings, templates, static files, API keys)

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# keep dev-safe secret key
SECRET_KEY = 'dev-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

# installed apps
# https://docs.djangoproject.com/en/1.8/intro/tutorial01/
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'internships',
]

# https://docs.djangoproject.com/en/5.2/topics/http/middleware/
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'internshipfinder.urls'

# https://djangocentral.com/configuring-django-templates/
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'internshipfinder.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# static files (im just using css)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "internships" / "static"]

# auth redirects
LOGIN_REDIRECT_URL = "/results/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "/login/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# django settings & environment variables
# https://docs.djangoproject.com/en/stable/howto/deployment/checklist/

# python os.environ tutorial
# https://docs.python.org/3/library/os.html#os.environ

# adzuna API APP_ID and APP_KEY
# https://developer.adzuna.com/overview

# Adzuna API
ADZUNA_APP_ID = os.environ.get("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.environ.get("ADZUNA_APP_KEY", "")
# Country code
ADZUNA_COUNTRY = os.environ.get("ADZUNA_COUNTRY", "us")

