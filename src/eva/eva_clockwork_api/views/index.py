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
from sol_lib.json_api_framework.endpoint.api_endpoint import api_endpoint

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewIndex(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse:
        return JsonResponse({"result":True})