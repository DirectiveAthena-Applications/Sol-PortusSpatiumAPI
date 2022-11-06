# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports
from json_framework.json_encoder import include_in_encoder
from custom_models.char_models import LowerCaseCharField

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@include_in_encoder
class StreamTag(models.Model):
    name = LowerCaseCharField(max_length=25)
