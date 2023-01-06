# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports
from eva_clockwork_api.models.action_category import ActionCategory

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Action(models.Model):
    timestamp_start = models.CharField(null=False)
    timestamp_duration = models.CharField(null=False)
    category = models.ForeignKey(ActionCategory, on_delete=models.RESTRICT, null=False, blank=False, default=None)