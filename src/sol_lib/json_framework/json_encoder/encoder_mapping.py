# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models
from django.db.models.fields import related_descriptors
from django.db.models.fields import related
from django.conf import settings
from typing import ClassVar, Callable
import datetime

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
CAST_TO_STR = lambda obj, name : str(getattr(obj, name))
CAST_DATE_TO_STR = lambda obj, name: str(getattr(obj, name).isoformat())
CAST_TO_INT = lambda obj, name : int(getattr(obj, name))
CAST_MANY_TO_MANY = lambda obj, name: getattr(obj, name).all()
CAST_AS_IS = lambda obj, name: getattr(obj, name)

SKIP_MODEL_ATTR:set[str] = {
    "DoesNotExist", "MultipleObjectsReturned", "id","objects", "get_next_by_date", "get_previous_by_date"
}

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class EncoderMapping:
    mapping:ClassVar[dict] = {
        models.QuerySet : lambda obj: list(obj),
        datetime.timezone : lambda obj: str(obj),
    }

    @staticmethod
    def _assemble_object_callback(encoder_result:dict[str:Callable]) -> Callable:
        return lambda obj: {
            name: callback(obj, name) for name, callback in encoder_result.items()
        }

    @classmethod
    def match_model_fields(cls, model_type):
        encoder_result = {}
        for name, value in model_type.__dict__.items():
            if name.startswith("_") or name in SKIP_MODEL_ATTR:
                continue

            match value:
                case models.query_utils.DeferredAttribute(field=models.fields.CharField()):
                    encoder_result[name] = CAST_TO_STR
                case models.query_utils.DeferredAttribute(field=models.fields.UUIDField()):
                    encoder_result[name] = CAST_TO_STR
                case models.query_utils.DeferredAttribute(field=models.fields.DateField()):
                    encoder_result[name] = CAST_DATE_TO_STR
                case models.query_utils.DeferredAttribute(field=models.fields.PositiveIntegerField()):
                    encoder_result[name] = CAST_TO_INT

                case models.fields.related_descriptors.ForwardManyToOneDescriptor(field=models.fields.related.ForeignKey()):
                    encoder_result[name] = CAST_AS_IS
                case models.fields.related_descriptors.ManyToManyDescriptor(field=models.fields.related.ManyToManyField()):
                    encoder_result[name] = CAST_MANY_TO_MANY

                case models.fields.related_descriptors.ForeignKeyDeferredAttribute():
                    continue
                case _:
                    if settings.DEBUG:
                        raise NotImplementedError(
                            f"the following was not implemented into the encoder:\n{name=}\n{value=}\n{value.__dict__=}")
                    continue

        # noinspection PyTypeChecker
        cls.mapping[model_type] = cls._assemble_object_callback(encoder_result)

        return model_type