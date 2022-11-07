# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views import View
import json

# Athena Packages

# Local Imports
from json_framework.api_endpoint import api_endpoint
from json_framework.api_response import ApiResponse

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewIndex(View):
    """
    Index of the streaming section of the Portus Spatium API
    """
    @api_endpoint
    def get(self, request:WSGIRequest) -> JsonResponse|ApiResponse:
        with open("docs/index.json", "r") as file:
            data = json.load(file)

        caught = []
        for url_data in data:
            if url_data["url"].startswith("api/streaming"):
                caught.append(url_data)

        return ApiResponse(caught)