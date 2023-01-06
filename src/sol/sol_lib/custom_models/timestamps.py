# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
re_timestamp:re.Pattern = re.compile(
    r"^((\d{4,})|(-\d{4,})|\+0000)-[0,1]\d-[0-3]\d(T[0-2]\d:[0-5]\d:[0-5]\d)?$"
)
re_duration:re.Pattern = re.compile(
    r"^P(\d+Y)?(\d+M)?(\d+D)?(T([1-23]H)?([1-59]M)?([1-59]S))?$"
)

def validate_timestamp(value:str) -> None:
    """
    Validates the inserted argument as a timestamp
    Raises a ValidationError if the value doesn't adhere to the ISO 8601 format
    """
    if not isinstance(value, str):
        raise ValidationError(gettext_lazy(f'{value} is not a string'))
    if not re_timestamp.match(value):
        raise ValidationError(gettext_lazy(f'{value} is not able to be defined as a timestamp in the ISO 8601 format'))

def validate_duration(value:str) -> None:
    """
    Validates the inserted argument as a duration
    Raises a ValidationError if the value doesn't adhere to the ISO 8601 format
    """
    if not isinstance(value, str):
        raise ValidationError(gettext_lazy(f'{value} is not a string'))
    if not re_duration.match(value):
        raise ValidationError(gettext_lazy(f'{value} is not able to be defined as a duration in the ISO 8601 format'))

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# class ISO8601_Timestamp(models.CharField):
#     default_validators = [validate_timestamp]
#
# class ISO8601_Duration(models.CharField):
#     default_validators = [validate_duration]