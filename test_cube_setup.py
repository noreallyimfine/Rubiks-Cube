import unittest
from cube import RubiksCube

class CubeSetupTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_color_count(self):

        # make sure there are 9 of each color