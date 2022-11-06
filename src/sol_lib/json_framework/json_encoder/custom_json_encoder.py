# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.functional import Promise
from django.db import models
import datetime
import uuid
import decimal
from typing import Any, Callable
import json
from dataclasses import dataclass

# Athena Packages

# Local Imports
from json_framework.json_encoder.encoder_mapping import EncoderMapping

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
_django_encoder: set[type] = {
    datetime.datetime, datetime.date, datetime.time, datetime.timedelta, uuid.UUID, decimal.Decimal, Promise
}

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CustomJsonEncoder(DjangoJSONEncoder):
    def default(self, o) -> Any:

        # for types already handled by Django:
        #   means I don't have to implement these by hand
        if type(o) in _django_encoder:
            return DjangoJSONEncoder.default(self,o)

        # For custom created models
        elif encode_callback := EncoderMapping.mapping.get(type(o), False):
            return encode_callback(o)

        # raises the correct type error
        else:
            return json.JSONEncoder.default(self, o)

