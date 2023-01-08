# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.exceptions import ValidationError
from django.db import transaction, DatabaseError
from django.test import TestCase
import json

# Athena Packages
from eva_clockwork_api.models.action import Action
from eva_clockwork_api.models.action_category import ActionCategory

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
def get_data_dict() -> dict:
    with open(file="tests/data/eva_clockwork_api/actions.json") as file:
        return json.load(file)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ActionTestCase(TestCase):
    categories:dict[str,ActionCategory]

    def setUp(self) -> None:
        self.categories = {
            "streaming":ActionCategory.objects.create(name="streaming")
        }
        self.data = get_data_dict()

    def test_valid(self):
        for kwarg in self.data["valid"]:
            with self.subTest(kwarg=kwarg):
                category = kwarg.pop("category")
                action:Action = Action.objects.create(**kwarg)
                action.category.add(self.categories[category])
                action.full_clean()
                action.save()

    def test_invalid(self):
        for kwarg in self.data["invalid"]:
            with self.subTest(kwarg=kwarg):
                category = kwarg.pop("category")
                # noinspection PyTypeChecker
                with self.assertRaises((DatabaseError,ValidationError)):
                    with transaction.atomic():
                        action:Action = Action.objects.create(**kwarg)
                        action.category.add(self.categories[category])
                        action.full_clean()
                        action.save()