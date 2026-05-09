"""Provider registry for future expansion."""

from typing import Optional


class Provider:
    """Base provider class for future API integration."""
    name: str
    base_url: str

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key
