import unittest
from core.pico_placa_rule import PicoPlacaRule
from datetime import time

class TestPlateParser(unittest.TestCase):

    def setUp(self):
        self.rule = PicoPlacaRule(
            day='Tuesday',
            plates_restricted=[1, 2],
            time_ranges=[(time(6, 0), time(9, 0)), (time(16, 0), time(20, 0))]
        )

    def test_restricted_time_and_day(self):
        """Restricted plate"""
        test_time = time(8, 0)
        test_day = 'Tuesday'
        result = self.rule.verify_pico_placa(last_digit=1, day_input=test_day, time_input=test_time)
        self.assertTrue(result)

    def test_outside_time_range(self):
        """Day of restriction out of restriction hours"""
        test_time = time(10, 0)
        test_day = 'Tuesday'
        result = self.rule.verify_pico_placa(last_digit=1, day_input=test_day, time_input=test_time)
        self.assertFalse(result)


    def test_not_restricted_plate_digit(self):
        """Not the day of restriction"""
        test_time = time(8, 0)
        test_day = 'Tuesday'
        result = self.rule.verify_pico_placa(last_digit=3, day_input=test_day, time_input=test_time)
        self.assertFalse(result)

    def test_edge_of_time_range_start(self):
        """Edge of restriction begining """
        test_time = time(6, 0)
        test_day = 'Tuesday'
        result = self.rule.verify_pico_placa(last_digit=2, day_input=test_day, time_input=test_time)
        self.assertTrue(result)

    def test_edge_of_time_range_end(self):
        """Edge of restriction end """
        test_time = time(20, 0)
        test_day = 'Tuesday'
        result = self.rule.verify_pico_placa(last_digit=2, day_input=test_day, time_input=test_time)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
