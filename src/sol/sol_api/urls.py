# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.contrib import admin
from django.urls import path, include

# Athena Packages

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    path('eva/clockwork/api', include('eva_clockwork_api.urls')),
    path('admin/',admin.site.urls),
]
