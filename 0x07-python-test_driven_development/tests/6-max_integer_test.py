#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, -7, 6, 4]), 6)
        self.assertAlmostEqual(max_integer([-7, 1, 6, 4]), 6)
        self.assertAlmostEqual(max_integer([-8, 4]), 4)
