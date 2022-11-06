# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.http import JsonResponse, HttpRequest
from django.db import transaction
from django.core import exceptions as DjangoExceptions
from django.views import View
from django.core.handlers.wsgi import WSGIRequest

# Athena Packages

# Local Imports
from json_framework.json_responses import BAD_REQUEST, SERVER_ERROR, NOT_ACCEPTABLE_JSON
from json_framework.api_response import ApiResponse
from json_framework.json_encoder import CustomJsonEncoder

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def api_endpoint(_fnc=None, *, validation_error:JsonResponse=BAD_REQUEST, object_does_not_exist:JsonResponse=BAD_REQUEST):
    # ------------------------------------------------------------------------------------------------------------------
    def decorator(fnc):
        def wrapper(obj:View, request:HttpRequest) -> JsonResponse:
            try:
                with transaction.atomic():
                    if not (content_type := request.headers.get("Content-Type", False)) or content_type != "application/json":
                        return NOT_ACCEPTABLE_JSON

                    match result := fnc(obj, request):
                        case ApiResponse(status=status):
                            # This is the only point where a result queryset can be encoded into a json,
                            #   therefor this is the only place to use the CustomJsonEncoder
                            return JsonResponse(result.to_dict(), status=status, encoder=CustomJsonEncoder)
                        case JsonResponse():
                            return result
                        case _:
                            return SERVER_ERROR

            except DjangoExceptions.ValidationError:
                return validation_error

            except DjangoExceptions.ObjectDoesNotExist:
                return object_does_not_exist

        return wrapper

    # ------------------------------------------------------------------------------------------------------------------
    # this allows the decorator to be used with or without `()`
    if _fnc is not None:
        return decorator(_fnc)
    else:
        return decorator
