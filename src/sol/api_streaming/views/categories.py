# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
import functools

from django.core.handlers.wsgi import HttpRequest
from django.http import JsonResponse
from django.views import View

# Athena Packages

# Local Imports
from json_framework.api_endpoint import api_endpoint
from json_framework.api_response import ApiResponse
from json_framework.json_responses import NOT_ACCEPTABLE_JSON
from api_streaming.models.category import StreamCategory

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class ValidatorPattern:
    hash:int
    __slots__ = ["hash"]

    def __init__(self, **kwargs):
        self.hash = hash(frozenset(kwargs.items()))

    @classmethod
    def from_request_body(cls, data_dict:dict):
        return cls(**{k:type(v) for k,v in data_dict.items()})


def validate_request_data(*, pattern:ValidatorPattern):
    def decorator(fnc):
        @functools.wraps(fnc)
        def wrapper(obj:ViewCategories, request:HttpRequest) -> JsonResponse:
            # Create the pattern,
            to_be_validated_pattern = ValidatorPattern.from_request_body(
                json_parsed_body := json.loads(request.body)
            )
            if pattern.hash == to_be_validated_pattern.hash:
                return fnc(obj, request, json_parsed_body=json_parsed_body)
            else:
                return NOT_ACCEPTABLE_JSON
        return wrapper
    return decorator

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewCategories(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse|ApiResponse:
        return ApiResponse(StreamCategory.objects.all())

    @api_endpoint
    @validate_request_data(pattern=ValidatorPattern(name=str, twitch_id=int))
    def post(self, request:HttpRequest, json_parsed_body:dict=None) -> JsonResponse|ApiResponse:
        stream_category = StreamCategory(**json_parsed_body if json_parsed_body is not None else json.loads(request.body))
        stream_category.full_clean()
        stream_category.save()
        return ApiResponse(stream_category)

