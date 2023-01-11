# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.urls import path

# Athena Packages

# Local Imports
from eva_clockwork_api.views.index import ViewIndex
from eva_clockwork_api.views.action import ViewAction

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path("", ViewIndex.as_view()),
    path("action", ViewAction.as_view())
]