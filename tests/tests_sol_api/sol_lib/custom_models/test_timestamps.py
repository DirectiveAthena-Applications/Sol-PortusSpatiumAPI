# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from django.core.exceptions import ValidationError
from django.test import TestCase
from typing import Iterable
import itertools
import json
import re

# Athena Packages
from sol_lib.custom_models.timestamps import re_timestamp, re_duration, validate_timestamp, validate_duration

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
invalid_data:Iterable = (
    [
        {"",0},
        {"":0},
        ["", 0],
        ("",0),
        0b01,
        0o21,
    ],
    range(0,256),
    range(-255,0),
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestRegexTimestamps(TestCase):
    @staticmethod
    def get_data_dict() -> dict:
        with open(file="tests/data/sol_lib/regex_timestamps_and_durations.json") as file:
            return json.load(file)

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the Regex Patterns -
    # ------------------------------------------------------------------------------------------------------------------
    def test_timestamp_valid(self):
        for timestamp in self.get_data_dict()["timestamp"]["valid"]:
            with self.subTest(timestamp=timestamp):
                self.assertIsInstance(re_timestamp.match(timestamp), re.Match)

    def test_timestamp_invalid(self):
        for timestamp in self.get_data_dict()["timestamp"]["invalid"]:
            with self.subTest(timestamp=timestamp):
                self.assertIsNone(re_timestamp.match(timestamp))

    # ------------------------------------------------------------------------------------------------------------------
    def test_duration_valid(self):
        for duration in self.get_data_dict()["duration"]["valid"]:
            with self.subTest(duration=duration):
                self.assertIsInstance(re_duration.match(duration), re.Match)

    def test_duration_invalid(self):
        for duration in self.get_data_dict()["duration"]["invalid"]:
            with self.subTest(duration=duration):
                self.assertIsNone(re_duration.match(duration))

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the validator functions -
    # ------------------------------------------------------------------------------------------------------------------
    def test_validation_timestamp_valid(self):
        for timestamp in self.get_data_dict()["timestamp"]["valid"]:
            with self.subTest(timestamp=timestamp):
                validate_timestamp(timestamp)

    def test_validation_timestamp_invalid(self):
        for timestamp in itertools.chain(
            self.get_data_dict()["timestamp"]["invalid"],
            invalid_data
        ):
            with self.subTest(timestamp=timestamp):
                with self.assertRaises(ValidationError):
                    validate_timestamp(timestamp)

    # ------------------------------------------------------------------------------------------------------------------
    def test_validation_duration_valid(self):
        for duration in self.get_data_dict()["duration"]["valid"]:
            with self.subTest(duration=duration):
                validate_duration(duration)

    def test_validation_duration_invalid(self):
        for duration in itertools.chain(
            self.get_data_dict()["timestamp"]["invalid"],
            invalid_data
        ):
            with self.subTest(duration=duration):
                with self.assertRaises(ValidationError):
                    validate_duration(duration)
