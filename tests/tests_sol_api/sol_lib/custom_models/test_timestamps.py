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
from sol_lib.custom_models.timestamps import (
    re_timestamp, re_duration, validate_timestamp, validate_duration,
    ISO8601_Timestamp, ISO8601_Duration
)

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
invalid_data:Iterable = (
    {"",0},     # set
    {"":0},     # dict
    ["", 0],    # list
    ("",0),     # tuple
    0b01,       # bin
    0o01,       # ovt
    -1,
    1,
    0,
    b"data",    # bytes instead of string
)

def get_data_dict() -> dict:
    with open(file="tests/data/sol_lib/regex_timestamps_and_durations.json") as file:
        return json.load(file)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestRegex(TestCase):
    def test_timestamp_valid(self):
        for timestamp in get_data_dict()["timestamp"]["valid"]:
            with self.subTest(timestamp=timestamp):
                self.assertIsInstance(re_timestamp.match(timestamp), re.Match)

    def test_timestamp_invalid(self):
        for timestamp in get_data_dict()["timestamp"]["invalid"]:
            with self.subTest(timestamp=timestamp):
                self.assertIsNone(re_timestamp.match(timestamp))

    # ------------------------------------------------------------------------------------------------------------------
    def test_duration_valid(self):
        for duration in get_data_dict()["duration"]["valid"]:
            with self.subTest(duration=duration):
                self.assertIsInstance(re_duration.match(duration), re.Match)

    def test_duration_invalid(self):
        for duration in get_data_dict()["duration"]["invalid"]:
            with self.subTest(duration=duration):
                self.assertIsNone(re_duration.match(duration))

# ----------------------------------------------------------------------------------------------------------------------
class TestValidators(TestCase):
    def test_validation_timestamp_valid(self):
        for timestamp in get_data_dict()["timestamp"]["valid"]:
            with self.subTest(timestamp=timestamp):
                validate_timestamp(timestamp)

    def test_validation_timestamp_invalid(self):
        for timestamp in itertools.chain(
            get_data_dict()["timestamp"]["invalid"],
            invalid_data
        ):
            with self.subTest(timestamp=timestamp):
                with self.assertRaises(ValidationError):
                    validate_timestamp(timestamp)

    # ------------------------------------------------------------------------------------------------------------------
    def test_validation_duration_valid(self):
        for duration in get_data_dict()["duration"]["valid"]:
            with self.subTest(duration=duration):
                validate_duration(duration)

    def test_validation_duration_invalid(self):
        for duration in itertools.chain(
            get_data_dict()["duration"]["invalid"],
            invalid_data
        ):
            with self.subTest(duration=duration):
                with self.assertRaises(ValidationError):
                    validate_duration(duration)

# ----------------------------------------------------------------------------------------------------------------------
class TestModels(TestCase):
    def setUp(self) -> None:
        pass # The timestamps and duration models don't need any pre-existing data to run the checks

    def test_ISO8601_Timestamp_valid(self):
        for timestamp in get_data_dict()["timestamp"]["valid"]:
            with self.subTest(timestamp=timestamp):
                ISO8601_Timestamp().run_validators(timestamp)

    def test_ISO8601_Timestamp_invalid(self):
        for timestamp in itertools.chain(
            get_data_dict()["timestamp"]["invalid"],
            invalid_data
        ):
            with self.subTest(timestamp=timestamp):
                with self.assertRaises(ValidationError):
                    ISO8601_Timestamp().run_validators(timestamp)

    # ------------------------------------------------------------------------------------------------------------------
    def test_ISO8601_Duration_valid(self):
        for duration in get_data_dict()["duration"]["valid"]:
            with self.subTest(timestamp=duration):
                ISO8601_Duration().run_validators(duration)

    def test_ISO8601_Duration_invalid(self):
        for duration in itertools.chain(
            get_data_dict()["duration"]["invalid"],
            invalid_data
        ):
            with self.subTest(duration=duration):
                with self.assertRaises(ValidationError):
                    ISO8601_Duration().run_validators(duration)
