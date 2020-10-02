#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    using unittest for testing a module
    """
    def test_integers(self):
        new_list = [1, 2, 3, 4]
        new_listb = [200, 500, 100,600]
        new_listc = [10]
        new_listd = [1200, 600, 300, 100]
        self.assertEqual(max_integer(new_list), 4)
        self.assertEqual(max_integer(new_listb), 600)
        self.assertEqual(max_integer(new_listc), 10)
        self.assertEqual(max_integer(new_listd), 1200)

    def test_negative_integers(self):
        new_list = [-5, -200, -1000, -2]
        new_listb = [-2, -2, -2, -2]
        self.assertEqual(max_integer(new_list), -2)
        self.assertEqual(max_integer(new_list), -2)

    def test_float_integers(self):
        new_list = [5.2, 5.1, 5.5, 5.3]
        new_listb = [20.11, 21.12, 21.11, 20.12]
        self.assertEqual(max_integer(new_list), 5.5)
        self.assertEqual(max_integer(new_listb), 21.12)

    def test_infinite_num(self):
        new_list = [1, 10, 100, 1000, float("inf")]
        self.assertEqual(max_integer(new_list), float("inf"))

    def test_str_parameter(self):
        new_list = ["1", "2", "a", "5"]
        new_listb = ["A", "B", "C", "Z"]
        self.assertEqual(max_integer(new_list), "a")
        self.assertEqual(max_integer(new_listb), "Z")

    def test_emptylist(self):
        new_list = []
        self.assertEqual(max_integer(new_list), None)

    def test_othertype(self):
        new_list = "Holberton"
        self.assertRaises(max_integer(new_list))
