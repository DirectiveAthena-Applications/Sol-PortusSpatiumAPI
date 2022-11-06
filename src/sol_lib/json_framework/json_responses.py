# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.http import JsonResponse

# Athena Packages

# Local Imports
from json_framework.api_response import ApiResponse

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
BAD_REQUEST: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Bad Request"], status=400)).to_dict(),
    status=response.status
)
ENDPOINT_NOT_FOUND: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Endpoint Not Found"], status=404)).to_dict(),
    status=response.status
)
NOT_ACCEPTABLE_JSON: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["JSON could not be found"], status=406)).to_dict(),
    status=response.status
)

SERVER_ERROR: JsonResponse = JsonResponse(
    (response := ApiResponse(errors=["Internal Server Error"], status=500)).to_dict(),
    status=response.status
)

