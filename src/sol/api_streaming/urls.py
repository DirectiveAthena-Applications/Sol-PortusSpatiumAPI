# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.urls import path

# Athena Packages

# Local Imports
from api_streaming.views.logs import ViewLogs
from api_streaming.views.platforms import ViewPlatform
from api_streaming.views.tags import ViewTags
from api_streaming.views.categories import ViewCategories

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path("logs", ViewLogs.as_view()),
    path("platforms", ViewPlatform.as_view()),
    path("tags", ViewTags.as_view()),
    path("categories", ViewCategories.as_view()),
]