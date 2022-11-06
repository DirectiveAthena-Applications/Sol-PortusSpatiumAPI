# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
ENDPOINT_NOT_FOUND: JsonResponse = JsonResponse(
    {
        "result":None,
        "errors":["endpoint not found"]
    },
    status=404
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class JsonView(View):

    def get(self, request:WSGIRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def post(self, request:WSGIRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def put(self, request:WSGIRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def patch(self, request:WSGIRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def delete(self, request:WSGIRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND