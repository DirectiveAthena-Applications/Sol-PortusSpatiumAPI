# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.db import models
import uuid

# Athena Packages

# Local Imports
from json_framework.json_encoder import include_in_encoder
from api_streaming.models.category import StreamCategory
from api_streaming.models.tag import StreamTag
from api_streaming.models.platform import StreamPlatform

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@include_in_encoder
class StreamLog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    date = models.DateField()
    day_of_streaming = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(null=True, blank=True, default=None)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.RESTRICT)
    category = models.ForeignKey(StreamCategory, on_delete=models.RESTRICT, null=True, blank=True, default=None)
    tags = models.ManyToManyField(StreamTag)
    youtube_link = models.URLField(null=True, blank=True)
