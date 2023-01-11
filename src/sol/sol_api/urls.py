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
    # Django stuff
    path('admin/',admin.site.urls),

    # Oath 2
    path(r'o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # EVA Apps
    path('eva/clockwork/api/', include('eva_clockwork_api.urls')),
]
