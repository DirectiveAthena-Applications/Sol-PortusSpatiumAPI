# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse

# Athena Packages

# Local Imports
from json_framework.view import JsonAPIView
from json_framework.api_endpoint import api_endpoint
from json_framework.api_response import ApiResponse

from api_streaming.models.log import StreamLog

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewIndex(JsonAPIView):
    @api_endpoint
    def get(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        return ApiResponse(StreamLog.objects.all())