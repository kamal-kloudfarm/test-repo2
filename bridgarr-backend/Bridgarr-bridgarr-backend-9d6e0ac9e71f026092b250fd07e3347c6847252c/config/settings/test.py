# ruff: noqa: F405,F403,E402
from .base import *

DEBUG = True

ALLOWED_HOSTS: list[str] = ["*"]
CORS_ALLOW_ALL_ORIGINS = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
