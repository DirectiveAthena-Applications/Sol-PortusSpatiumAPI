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
class AppEvaClockworkAPI(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eva_clockwork_api'
    verbose_name = "EVA Clockwork API"
