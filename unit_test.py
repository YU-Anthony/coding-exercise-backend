#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import pandas as pd
from getPointBalances import calculate

class TestCalculate(unittest.TestCase):

    def setUp(self):
        self.points = 5000
        self.expected_result = {
            "DANNON": 1000, 
            "UNILEVER": 0, 
            "MILLER COORS": 5300 
        }

        self.data = pd.DataFrame({
            "payer": ["DANNON", "UNILEVER", "DANNON", "MILLER COORS", "DANNON"],
            "points": [1000, 200, -200, 10000, 300],
            "timestamp": ["2020-11-02T14:00:00Z", "2020-10-31T11:00:00Z", "2020-10-31T15:00:00Z", "2020-11-01T14:00:00Z", "2020-10-31T10:00:00Z"]
        })

    def test_calculate(self):
        ans = calculate(self.points)
        self.assertEqual(ans, self.expected_result)

    def test_negative_points(self):
        with self.assertRaises(Exception) as context:
            calculate(-1000)
        self.assertEqual(str(context.exception), "The points can not be negative.")

    def test_no_input_points(self):
        with self.assertRaises(Exception) as context:
            calculate(None)
        self.assertEqual(str(context.exception), "Plase input the value of points that you want to spend")

if __name__ == '__main__':
    unittest.main()