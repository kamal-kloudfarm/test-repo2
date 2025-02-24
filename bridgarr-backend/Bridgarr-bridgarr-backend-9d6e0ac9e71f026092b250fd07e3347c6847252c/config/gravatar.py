"""Gravatar utilities"""

import hashlib
from urllib.parse import urlencode

from django.templatetags.static import static

# Set your variables here


def get_gravatar(email: str, default: str | None = None, size: int = 80) -> str:
    if not default:
        default = static("img/default-avatar.png")
    """Return the Gravatar URL for the given email."""
    email_encoded = email.lower().encode("utf-8")
    email_hash = hashlib.sha256(email_encoded).hexdigest()
    query_params = urlencode({"d": default, "s": str(size)})
    return f"https://www.gravatar.com/avatar/{email_hash}?{query_params}"
