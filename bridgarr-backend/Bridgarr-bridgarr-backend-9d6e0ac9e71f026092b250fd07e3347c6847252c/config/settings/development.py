# ruff: noqa: F405,F403,E402
from .base import *

DEBUG = True

ALLOWED_HOSTS: list[str] = ["*"]
CORS_ALLOWED_ORIGINS: list[str] = getlistenv("CORS_ALLOWED_ORIGINS")
CORS_ALLOW_CREDENTIALS = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
