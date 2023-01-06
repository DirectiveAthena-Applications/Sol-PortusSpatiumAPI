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
class App_EvaClockworkAPI_Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eva_clockwork_api'
    verbose_name = "EVA Clockwork API"
