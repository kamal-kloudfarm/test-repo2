# ruff: noqa: F405,F403,E402
from config.env import getlistenv

from .base import *

PLUNK_API_KEY = getenv("PLUNK_API_KEY")
PLUNK_API_URL = getenv("PLUNK_API_URL")

DEBUG = False
ALLOWED_HOSTS: list[str] = getlistenv("DJANGO_ALLOWED_HOSTS")
CORS_ALLOWED_ORIGINS: list[str] = getlistenv("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_CREDENTIALS = True

EMAIL_BACKEND = "config.plunk.PlunkEmailBackend"
INSTALLED_APPS += ["django_backblaze_b2"]
STORAGES.update(
    {
        "default": {
            "BACKEND": "django_backblaze_b2.storages.LoggedInStorage",
        }
    }
)

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
    "django-backblaze-b2": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache"
    },
}


from .vendor.backblaze import *
