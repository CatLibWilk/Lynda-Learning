# myproject/settings/dev.py
from ._base import *
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEBUG = True
WEBSITE_URL = "http://127.0.0.1:8000"  # without trailing slash