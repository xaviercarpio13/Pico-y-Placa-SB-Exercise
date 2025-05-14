import unittest
from utils.plate_parser import PlateParser

class TestPlateParser(unittest.TestCase):

    def test_valid_plate(self):
        """Valid licence plate."""
        self.assertTrue(PlateParser.validator_licence_plate("ABC-1234"))

    def test_invalid_plate_short_letters(self):
        """Invalid licence plate: Not enough letters"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("AB-1234")

    def test_invalid_plate_short_numbers(self):
        """Invalid licence plate: Not enough numbers"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("ABC-123")

    def test_invalid_plate_no_dash(self):
        """Invalid licence plate: Not middle dash"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("ABC1234")

    def test_invalid_plate_lowercase(self):
        """Invalid licence plate: lowercase"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("abc-1234")

    def test_invalid_plate_extra_characters(self):
        """Invalid licence plate: Aditional characters"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("ABCD-1234")

    def test_invalid_plate_special_characters(self):
        """Invalid licence plate: special characters"""
        with self.assertRaises(ValueError):
            PlateParser.validator_licence_plate("A*C-1234")

if __name__ == '__main__':
    unittest.main()
