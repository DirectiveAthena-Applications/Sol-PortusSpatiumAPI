# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.test import TestCase

# Athena Packages
from eva_clockwork_api.models.action import Action
from eva_clockwork_api.models.action_category import ActionCategory

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ActionTestCase(TestCase):

    def setUp(self) -> None:
        category_streaming = ActionCategory.objects.create(name="streaming")
        action = Action.objects.create(
            timestamp="2023-01-08T15:21:00",
            duration="P5H",
            subject="[BE] Relearning Django day 2 | After weeks of being ill, I'm back and hyper on coffee ☕",
            note="This is a test",
            mood=5,
        )
        action.category.add(category_streaming)

    def test_test(self):
        action_2023_01_08:Action = Action.objects.get(timestamp="2023-01-08T15:21:00")

        self.assertEqual(
            action_2023_01_08.duration, "P5H"
        )