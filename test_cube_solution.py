import unittest
from cube import RubiksCube

# rename that class
class CubeTurnTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()
