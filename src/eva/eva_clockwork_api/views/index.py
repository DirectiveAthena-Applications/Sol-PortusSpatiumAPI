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

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewIndex(View):
    def get(self, request:HttpRequest) -> JsonResponse:
        return JsonResponse({"result":True})