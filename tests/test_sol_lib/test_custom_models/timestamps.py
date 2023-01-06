# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import re
import unittest

# Athena Packages
from sol_lib.custom_models.timestamps import re_timestamp, re_duration, validate_timestamp, validate_duration

# Local Imports

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestRegexTimestamps(unittest.TestCase):
    def test_timestamp_true(self):
        strings_timestamps: list[str] = [
            "2023-01-06",
            "-0100-01-06",
            "20000-08-12",
            "+0000-12-12",
            "-0001-04-24",
            "0846-07-28"
        ]
        for timestamp in strings_timestamps:
            with self.subTest(timestamp=timestamp):
                self.assertIsInstance(re_timestamp.match(timestamp), re.Match)

    def test_timestamp_false(self):
        strings_timestamps: list[str] = [
            "800-01-01",
            "20000-28-12",
            "1000-24-55",
            "1000-12-55"
        ]
        for timestamp in strings_timestamps:
            with self.subTest(timestamp=timestamp):
                self.assertIsNone(re_timestamp.match(timestamp))

    # ------------------------------------------------------------------------------------------------------------------
    def test_duration_true(self):
        strings_durations: list[str] = [
            "P5Y",
            "P5Y11M",
            "P69Y10M24D",
            "P56489Y1D",
            "PT8H",
            "PT23H",
            "P8YT8H"
        ]
        for duration in strings_durations:
            with self.subTest(duration=duration):
                self.assertIsInstance(re_duration.match(duration), re.Match)

    def test_duration_false(self):
        strings_durations: list[str] = [
            "5Y",
            "P5Y32M",
        ]
        for duration in strings_durations:
            with self.subTest(duration=duration):
                self.assertIsNone(re_duration.match(duration))