# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports
from sol_lib.custom_models.char_models import LowerCaseCharField

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ActionCategory(models.Model):
    """
    Category of actions you are doing during a specific timeframe
    Name thanks to SaniSensei
    """

    name = LowerCaseCharField(max_length=32)