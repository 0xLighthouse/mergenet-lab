import unittest
from calculator import clamp
class Clamp(unittest.TestCase):
    def test_bounds(self):
        self.assertEqual(clamp(-1, 0, 10), 0)
        self.assertEqual(clamp(11, 0, 10), 10)
        self.assertEqual(clamp(5, 0, 10), 5)

    def test_invalid_bounds(self):
        with self.assertRaises(ValueError):
            clamp(5, 10, 0)

    def test_endpoints(self):
        self.assertEqual(clamp(0, 0, 10), 0)
        self.assertEqual(clamp(10, 0, 10), 10)
