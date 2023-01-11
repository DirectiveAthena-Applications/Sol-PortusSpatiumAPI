# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.handlers.wsgi import HttpRequest
from django.db.models import QuerySet
from django.http import JsonResponse
from django.views import View
from django.core import serializers


# Athena Packages

# Local Imports
from sol_lib.json_api_framework.endpoint.api_endpoint import api_endpoint
from eva_clockwork_api.models.action import Action
from eva_clockwork_api.models.action_category import ActionCategory
from sol_lib.json_api_framework.endpoint.prebuilt_json_responses import ENDPOINT_NOT_FOUND

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ApiEndpointView(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse:
        if request.user.is_authenticated:
            return self.get_authenticated(request)
        else:
            return self.get_anonymous(request)

    def get_authenticated(self, request:HttpRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

    def get_anonymous(self, request:HttpRequest) -> JsonResponse:
        return ENDPOINT_NOT_FOUND

class ApiAction(ApiEndpointView):

    def get_authenticated(self, request:HttpRequest) -> JsonResponse:
        pass

    def get_anonymous(self, request:HttpRequest) -> JsonResponse:
        pass

class ViewAction(View):
    @api_endpoint
    def get(self, request:HttpRequest) -> JsonResponse:

        category, _ =  ActionCategory.objects.get_or_create(name="streaming")
        action = Action(
            timestamp="2023-01-08T15:21:00",
            duration="PT5H",
            subject="[BE] Relearning Django day 2 | After weeks of being ill, I'm back and hyper on coffee ☕",
            note="This is a test",
            mood=5,
        )
        action.save()
        action.category.add(
            category
        )
        action.save()

        all_actions:QuerySet = Action.objects.all()

        data = serializers.serialize("json", all_actions)

        return JsonResponse({"result":data})