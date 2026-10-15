import importlib.util
import unittest
class Composition(unittest.TestCase):
    def test_enabled_features_are_compatible(self):
        a = importlib.util.find_spec('feature_a') is not None
        b = importlib.util.find_spec('feature_b') is not None
        if a:
            import feature_a
            self.assertIn(feature_a.VALUE, (1, 2))
        if b:
            import feature_b
            self.assertEqual(feature_b.VALUE, 1)
