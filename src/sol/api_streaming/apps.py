# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.apps import AppConfig

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AppStreamingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_streaming'
    verbose_name = "Streaming"
