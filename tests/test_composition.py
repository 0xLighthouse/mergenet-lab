import importlib.util
import unittest
class Composition(unittest.TestCase):
    def test_enabled_features_are_compatible(self):
        a = importlib.util.find_spec('feature_a') is not None
        b = importlib.util.find_spec('feature_b') is not None
        self.assertIsNone(importlib.util.find_spec("feature_f"), "poisoned stack F")
