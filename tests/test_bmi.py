#!/usr/bin/env python

"""Test for  bmiCalculator"""

import sys
import os
import unittest

from bmiCalculator.calculator import _get_bmi_df, _get_overweight_count

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


test_data = [{'Gender': 'Male', 'HeightCm': 150, 'WeightKg': 70},
             {'Gender': 'Female', 'HeightCm': 161, 'WeightKg': 70}, {'Gender': 'Male', 'HeightCm': 167, 'WeightKg': 82}]


class TestbmiCalculator(unittest.TestCase):
    """Test class for bmiCalculator"""

    def setUp(self) -> None:
        """Set up"""
        pass

    def test_get_bmi_df(self):
        test_data_bmi = _get_bmi_df(test_data)
        assert('BMI' in test_data_bmi.columns)
        assert('BMI_Category' in test_data_bmi.columns)
        assert('Health_Risk' in test_data_bmi.columns)
        assert(test_data_bmi['BMI'][2] == 29.4)
        assert(test_data_bmi['BMI_Category'][2] == 'OverWeight')
        assert(test_data_bmi['Health_Risk'][2] == 'Enhanced risk')
        assert(test_data_bmi['BMI'][0] == 31.1)
        assert(test_data_bmi['BMI_Category'][0] == 'Moderately obese')
        assert(test_data_bmi['Health_Risk'][0] == 'Medium risk')

    def test_get_overweight_count(self):
        test_data_bmi = _get_bmi_df(test_data)
        overweight_count = _get_overweight_count(df=test_data_bmi)
        assert(overweight_count == 2)
