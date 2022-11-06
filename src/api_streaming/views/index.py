# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.views import View
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ViewIndex(View):
    def get(self, request:WSGIRequest):
        return HttpResponse("HELLO WORLD")