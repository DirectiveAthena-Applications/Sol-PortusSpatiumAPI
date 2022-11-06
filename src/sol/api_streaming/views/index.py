# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views import View

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
        return ApiResponse(
            [
                {
                    "url": "api/streaming",
                    "doc": "Index of the streaming section of the Portus Spatium API",
                    "methods": ["GET"],
                    "pages": [
                        {
                            "url": "api/streaming/logs",
                            "doc": "Entry point to gather, post or edit logs",
                            "methods": ["GET", "POST", "DELETE", "PATCH"],
                            "pages": []
                        },
                        {
                            "url": "api/streaming/categories",
                            "doc": "Entry point to gather, post or edit streaming categories",
                            "methods": ["GET", "POST", "DELETE", "PATCH"],
                            "pages": []
                        }
                    ]
                }
            ]
        )