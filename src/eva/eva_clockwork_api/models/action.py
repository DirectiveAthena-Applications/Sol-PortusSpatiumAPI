# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Athena Packages

# Local Imports
from eva_clockwork_api.models.action_category import ActionCategory
from sol_lib.custom_models.timestamps import ISO8601_Timestamp, ISO8601_Duration

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Action(models.Model):
    timestamp = ISO8601_Timestamp(max_length=32,null=False, blank=False)
    duration = ISO8601_Duration(max_length=32,null=True)
    category = models.ManyToManyField(ActionCategory)
    subject = models.CharField(max_length=255, null=False, blank=False)
    note = models.TextField(null=True)
    mood = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    user = models.ForeignKey(User, on_delete=models.RESTRICT)