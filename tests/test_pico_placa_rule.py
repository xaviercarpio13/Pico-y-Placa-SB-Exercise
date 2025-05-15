import unittest
from datetime import time
from core.pico_placa_rule import PicoPlacaRule

class TestPicoPlacaRule(unittest.TestCase):

    def setUp(self):
        self.rule = PicoPlacaRule(
            day="Monday",
            plates_restricted=[1, 2],
            time_ranges=[("07:00", "09:30"), ("16:00", "19:30")]
        )

    def test_restricted_vehicle_within_time(self):
        """Restricted vehicle within the restriction time"""
        is_restricted, message = self.rule.verify_pico_placa("1", "Monday", "08:15")
        self.assertTrue(is_restricted)

    def test_restricted_vehicle_outside_time(self):
        """Restricted vehicle outside the restriction time"""
        is_restricted, message = self.rule.verify_pico_placa("1", "Monday", "10:00")
        self.assertFalse(is_restricted)

    def test_unrestricted_vehicle_on_restricted_day(self):
        """Unrestricted vehicle on a restricted day"""
        is_restricted, message = self.rule.verify_pico_placa("3", "Monday", "08:00")
        self.assertFalse(is_restricted)

    def test_vehicle_on_non_restricted_day(self):
        """Vehicle on a non-restricted day"""
        is_restricted, message = self.rule.verify_pico_placa("1", "Tuesday", "08:00")
        self.assertFalse(is_restricted)

    def test_restricted_vehicle_on_edge_of_range_start(self):
        """Restricted vehicle on the edge of the restriction time range"""
        is_restricted, message = self.rule.verify_pico_placa("2", "Monday", "07:00")
        self.assertTrue(is_restricted)

    def test_restricted_vehicle_on_edge_of_range_end(self):
        """Restricted vehicle on the edge of the restriction time range"""
        is_restricted, message = self.rule.verify_pico_placa("2", "Monday", "09:30")
        self.assertTrue(is_restricted)


if __name__ == '__main__':
    unittest.main()
