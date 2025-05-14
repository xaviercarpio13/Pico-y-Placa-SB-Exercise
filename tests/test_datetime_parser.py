import unittest
from utils.date_parser import DateParser
import datetime

class TestDateTimeParser(unittest.TestCase):

    def test_valid_datetime(self):
        """Valid date and time."""
        result = DateParser.validator_date_time("2023-12-15-14:45")
        self.assertTrue(result)

    def test_invalid_format_slashes(self):
        """Invalid date and time: using slashes instead of dashes."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2023/12/15-14:45")

    def test_invalid_format_missing_time(self):
        """Invalid date and time: missing time."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2023-12-15")

    def test_invalid_format_extra_chars(self):
        """Invalid date and time: extra characters."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2023-12-15-14:45:00")

    def test_invalid_date_nonexistent(self):
        """Invalid date: Feb 30 does not exist."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2021-02-30-09:00")

    def test_invalid_month(self):
        """Invalid month: 13 is out of range."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2023-13-10-12:00")

    def test_invalid_hour(self):
        """Invalid hour: 25 is out of range."""
        with self.assertRaises(ValueError):
            DateParser.validator_date_time("2023-10-10-25:00")

    def test_valid_leap_year(self):
        """Valid leap year date."""
        result = DateParser.validator_date_time("2024-02-29-08:00")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
