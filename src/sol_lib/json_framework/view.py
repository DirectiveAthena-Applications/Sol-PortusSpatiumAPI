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
from json_framework.json_responses import ENDPOINT_NOT_FOUND
from json_framework.api_endpoint import api_endpoint
from json_framework.api_response import ApiResponse

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class JsonAPIView(View):

    @api_endpoint
    def get(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ENDPOINT_NOT_FOUND

    @api_endpoint
    def post(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ENDPOINT_NOT_FOUND

    @api_endpoint
    def put(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ENDPOINT_NOT_FOUND

    @api_endpoint
    def patch(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ENDPOINT_NOT_FOUND

    @api_endpoint
    def delete(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ENDPOINT_NOT_FOUND