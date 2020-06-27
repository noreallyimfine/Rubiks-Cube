import unittest
from cube import RubiksCube

# rename that class
class CubeTurnTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

# test solution funcs <- make sure the tests arent interfering with each other
    
    def test_make_daisy(self):

        bottom_center = self.cube.bot_layer['bottom_center'].sides['bottom']

        self.cube._make_daisy()

        self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.top_layer['front_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.top_layer['back_middle'].sides['top'], bottom_center)
    
    def test_bottom_cross(self):

        bottom_center = self.cube.bot_layer['bottom_center'].sides['bottom']

        self.cube._bottom_cross()

        self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['top'], bottom_center)
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['top'], bottom_center)

    def test_bottom_layer(self):

        # all bottoms match the center
        bottom_center = self.cube.bot_layer['bottom_center'].sides['bottom']
        right_center = self.cube.mid_layer['right_center'].sides['right']
        left_center = self.cube.mid_layer['left_center'].sides['left']
        front_center = self.cube.mid_layer['front_center'].sides['front']
        back_center = self.cube.mid_layer['back_center'].sides['back']

        
        # all 'sides' match their corresponding center