# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import re
import unittest
from django.core.exceptions import ValidationError
import itertools
from typing import Iterable

# Athena Packages
from sol_lib.custom_models.timestamps import re_timestamp, re_duration, validate_timestamp, validate_duration

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
timestamps_valid:Iterable =[
    "2023-01-06",
    "-0100-01-06",
    "20000-08-12",
    "+0000-12-12",
    "-0001-04-24",
    "0846-07-28",
    "0513-11-12T00:12:05",
    "10000-12-08",
]
timestamps_invalid:Iterable = (
    (timestamps_invalid_re:=[
        "800-01-01",
        "20000-28-12",
        "1000-24-55",
        "1000-12-55",
        "0000-21-00",
        "0000-00-48",
        "0513-11-12T00:12:60",
        "0001-01-01T00:84:00",
        "3-01-01",
        "03-01-01",
        "003-01-01",
        "0001-1-1",
        "0001-January-01",
        "0001-Jan-01",
        "0001-Ja-01",
        "31-12-0001",
        "12-31-0001",
        "1999-31-12",
        "10_000-12-08",
    ]),
    [
        {"",0},
        ["", 0],
        ("",0),
        0b01,
        0o21,
    ],
    range(0,256),
    range(-255,0)
)
durations_valid:Iterable = [
    "P5Y",
    "P5Y11M",
    "P69Y10M24D",
    "P56489Y1D",
    "PT8H",
    "PT23H",
    "P8YT8H"
]
durations_invalid:Iterable = (
    (durations_invalid_re:=[
        "5Y",
        "P5Y32M",
    ]),
    [
        {"",0},
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
class TestRegexTimestamps(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the Regex Patterns -
    # ------------------------------------------------------------------------------------------------------------------
    def test_timestamp_valid(self):
        for timestamp in timestamps_valid:
            with self.subTest(timestamp=timestamp):
                self.assertIsInstance(re_timestamp.match(timestamp), re.Match)

    def test_timestamp_invalid(self):
        for timestamp in timestamps_invalid_re:
            with self.subTest(timestamp=timestamp):
                self.assertIsNone(re_timestamp.match(timestamp))

    # ------------------------------------------------------------------------------------------------------------------
    def test_duration_valid(self):
        for duration in durations_valid:
            with self.subTest(duration=duration):
                self.assertIsInstance(re_duration.match(duration), re.Match)

    def test_duration_invalid(self):
        for duration in durations_invalid_re:
            with self.subTest(duration=duration):
                self.assertIsNone(re_duration.match(duration))

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests for the validator functions -
    # ------------------------------------------------------------------------------------------------------------------
    def test_validation_timestamp_valid(self):
        for timestamp in timestamps_valid:
            with self.subTest(timestamp=timestamp):
                validate_timestamp(timestamp)

    def test_validation_timestamp_invalid(self):
        for timestamp in itertools.chain(*timestamps_invalid):
            with self.subTest(timestamp=timestamp):
                with self.assertRaises(ValidationError):
                    validate_timestamp(timestamp)

    # ------------------------------------------------------------------------------------------------------------------
    def test_validation_duration_valid(self):
        for duration in durations_valid:
            with self.subTest(duration=duration):
                validate_duration(duration)

    def test_validation_duration_invalid(self):
        for duration in itertools.chain(*durations_invalid):
            with self.subTest(duration=duration):
                with self.assertRaises(ValidationError):
                    validate_duration(duration)
