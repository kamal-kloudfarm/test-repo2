# ruff: noqa:E402,F403
import os
from pathlib import Path

import dj_database_url
from django.contrib.messages import constants as messages

from config.env import getenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = getenv("DJANGO_SECRET_KEY")

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

INSTALLED_APPS = [
    # Django
    "unfold",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd Party Libraries
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "social_django",
    "drf_spectacular",
    "django_extensions",
    "phonenumber_field",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    # Business Logic
    "apps.authentication",
    "apps.profile",
    # 'apps.wallet',
    # 'apps.vendor',
    # 'apps.contract',
]

SITE_ID = 1
AUTH_USER_MODEL = "authentication.User"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
ADMIN_URL = getenv("DJANGO_ADMIN_URL")


MESSAGE_TAGS = {
    messages.ERROR: "danger",
}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "config" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.AllowAllUsersModelBackend",
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.linkedin.LinkedinOpenIdConnect",
    "social_core.backends.twitter_oauth2.TwitterOAuth2",
]

WSGI_APPLICATION = "config.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [BASE_DIR / "config" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    },
}


IGNORED_LOGGERS = [
    "django.request",
    "django.db.backends",
    "faker",
    "asyncio",
    "django-backblaze-b2",
    "django_backblaze_b2",
    "b2sdk",
    "urllib3",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} [{name}] {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        **{
            logger: {
                "handlers": ["console"],
                "level": "ERROR",
                "propagate": False,
            }
            for logger in IGNORED_LOGGERS
        },
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },
}


from .vendor.djoser import *
from .vendor.drf import *
from .vendor.jwt import *
from .vendor.social import *
from .vendor.unfold import *
