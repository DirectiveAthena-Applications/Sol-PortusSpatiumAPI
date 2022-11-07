# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import inspect
from django.core.management.base import BaseCommand, CommandError
from django.urls import URLPattern
from django.views import View
import dataclasses
from dataclasses import dataclass, field
import json

# Athena Packages

# Local Imports
from api_streaming.urls import urlpatterns as api_streaming_url_patterns

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PATTERN_GROUPS = {
    "api/streaming" : api_streaming_url_patterns
}

KNOWN_HTTP_METHODS = ["get","post","put","patch","delete"]

@dataclass(slots=True)
class UrlData:
    url:str
    doc:str
    methods:list[str] = field(default_factory=list)
    pages:list[UrlData] = field(default_factory=list)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Command(BaseCommand):
    help = "Generates the index docs for the API endpoints"

    def handle(self, *args, **options):
        parsed_items:list[dict] = []

        for api_entry, urlpatterns in PATTERN_GROUPS.items():
            for url_pattern in urlpatterns: #type: URLPattern
                view:View = url_pattern.callback.view_class

                url_data = UrlData(
                    url=f"{api_entry}/{url_pattern.pattern}",
                    doc=inspect.cleandoc(docs) if (docs := view.__doc__) is not None else ""
                )
                
                # go over the known methods and add them to list
                for known_method in KNOWN_HTTP_METHODS:
                    if getattr(view, known_method, False):
                        url_data.methods.append(known_method)


                parsed_items.append(dataclasses.asdict(url_data))

        with open("docs/index.json", "w") as file:
            json.dump(parsed_items, file, indent=2)
