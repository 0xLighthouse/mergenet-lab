import unittest
from calculator import clamp
class Clamp(unittest.TestCase):
    def test_bounds(self):
        self.assertEqual(clamp(-1, 0, 10), 0)
        self.assertEqual(clamp(11, 0, 10), 10)
        self.assertEqual(clamp(5, 0, 10), 5)
