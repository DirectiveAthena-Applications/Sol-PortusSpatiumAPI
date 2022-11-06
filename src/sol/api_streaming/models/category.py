# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports
from json_framework.json_encoder import include_in_encoder

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@include_in_encoder
class StreamCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    twitch_id = models.PositiveIntegerField()