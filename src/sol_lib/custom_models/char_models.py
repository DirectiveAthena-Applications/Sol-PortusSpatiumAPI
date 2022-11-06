# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class LowerCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(LowerCaseCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).lower()

class UpperCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).upper()