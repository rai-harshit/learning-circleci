import unittest
import sys
import os

# Add the parent directory of the 'python' folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from python.app import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = add(3, -5)
        self.assertEqual(result, -2)
