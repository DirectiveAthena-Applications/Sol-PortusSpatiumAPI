# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import HttpRequest
from django.http import JsonResponse
from django.views import View

# Athena Packages

# Local Imports
from json_framework.api_endpoint import api_endpoint
from json_framework.api_response import ApiResponse
from api_streaming.models.log import StreamLog
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewLogs(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse|ApiResponse:
        return ApiResponse(StreamLog.objects.all())
