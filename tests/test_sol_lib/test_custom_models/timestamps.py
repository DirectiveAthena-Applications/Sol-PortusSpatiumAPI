# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import re
import unittest
from django.core.exceptions import ValidationError
import itertools
from typing import Any

# Athena Packages
from sol_lib.custom_models.timestamps import re_timestamp, re_duration, validate_timestamp, validate_duration

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestRegexTimestamps(unittest.TestCase):
    strings_timestamps_true: list[str] = [
        "2023-01-06",
        "-0100-01-06",
        "20000-08-12",
        "+0000-12-12",
        "-0001-04-24",
        "0846-07-28",
        "0513-11-12T00:12:05"
    ]
    strings_timestamps_false: list[str] = [
        "800-01-01",
        "20000-28-12",
        "1000-24-55",
        "1000-12-55",
        "0000-21-00",
        "0000-00-48",
        "0513-11-12T00:12:60",
        "0001-01-01T00:84:00",
    ]
    strings_durations_true: list[str] = [
        "P5Y",
        "P5Y11M",
        "P69Y10M24D",
        "P56489Y1D",
        "PT8H",
        "PT23H",
        "P8YT8H"
    ]
    strings_durations_false: list[str] = [
        "5Y",
        "P5Y32M",
    ]

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the Regex Patterns -
    # ------------------------------------------------------------------------------------------------------------------
    def test_timestamp_true(self):
        for timestamp in self.strings_timestamps_true:
            with self.subTest(timestamp=timestamp):
                self.assertIsInstance(re_timestamp.match(timestamp), re.Match)

    def test_timestamp_false(self):
        for timestamp in self.strings_timestamps_false:
            with self.subTest(timestamp=timestamp):
                self.assertIsNone(re_timestamp.match(timestamp))

    # ------------------------------------------------------------------------------------------------------------------
    def test_duration_true(self):
        for duration in self.strings_durations_true:
            with self.subTest(duration=duration):
                self.assertIsInstance(re_duration.match(duration), re.Match)

    def test_duration_false(self):
        for duration in self.strings_durations_false:
            with self.subTest(duration=duration):
                self.assertIsNone(re_duration.match(duration))

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the validator functions -
    # ------------------------------------------------------------------------------------------------------------------
    def test_validate_timestamp_true(self):
        extra_values:list[Any] = []
        for timestamp in itertools.chain(self.strings_timestamps_true, extra_values):
            with self.subTest(timestamp=timestamp):
                validate_timestamp(timestamp)

    def test_validate_timestamp_false(self):
        extra_values:list[Any] = [
            0,
            {"a"},
            ["a",],
            ("a",)
        ]
        for timestamp in itertools.chain(self.strings_timestamps_false, extra_values):
            with self.subTest(timestamp=timestamp):
                with self.assertRaises(ValidationError):
                    validate_timestamp(timestamp)

    # ------------------------------------------------------------------------------------------------------------------
    def test_validate_duration_true(self):
        extra_values:list[Any] = []
        for duration in itertools.chain(self.strings_durations_true, extra_values):
            with self.subTest(duration=duration):
                validate_duration(duration)

    def test_validate_duration_false(self):
        extra_values:list[Any] = [
            0,
            {"a"},
            ["a",],
            ("a",)
        ]
        for duration in itertools.chain(self.strings_durations_false, extra_values):
            with self.subTest(duration=duration):
                with self.assertRaises(ValidationError):
                    validate_duration(duration)
