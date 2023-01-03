import unittest

class TestMaxInteger:
    def test_max_integer(unittest.TestCase):
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([7,3,4,2]), 7)
