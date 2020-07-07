import unittest
from cube import RubiksCube

unittest.TestLoader.sortTestMethodsUsing = None

# rename that class
class CubeSolutionTests(unittest.TestCase):
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

        self.assertEqual(self.cube.bot_layer['right_middle'].sides['bottom'], bottom_center)
        self.assertEqual(self.cube.bot_layer['left_middle'].sides['bottom'], bottom_center)
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['bottom'], bottom_center)
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['bottom'], bottom_center)

        # also test the other sides match their face
        right_center = self.cube.mid_layer['right_center'].sides['right']
        left_center = self.cube.mid_layer['left_center'].sides['left']
        front_center = self.cube.mid_layer['front_center'].sides['front']
        back_center = self.cube.mid_layer['back_center'].sides['back']

        self.assertEqual(self.cube.bot_layer['right_middle'].sides['right'], right_center)
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['front'], front_center)
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['back'], back_center)
        self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], left_center)

    def test_bottom_layer(self):

        bottom_center = self.cube.bot_layer['bottom_center'].sides['bottom']
        right_center = self.cube.mid_layer['right_center'].sides['right']
        left_center = self.cube.mid_layer['left_center'].sides['left']
        front_center = self.cube.mid_layer['front_center'].sides['front']
        back_center = self.cube.mid_layer['back_center'].sides['back']

        self.cube._solve_bot_layer()

        # all bottoms match the center
        bottom_face = [
            self.cube.bot_layer['front_right'].sides['bottom'],
            self.cube.bot_layer['front_middle'].sides['bottom'],
            self.cube.bot_layer['front_left'].sides['bottom'],
            self.cube.bot_layer['back_left'].sides['bottom'],
            self.cube.bot_layer['back_right'].sides['bottom'],
            self.cube.bot_layer['back_middle'].sides['bottom'],
            self.cube.bot_layer['left_middle'].sides['bottom'],
            self.cube.bot_layer['right_middle'].sides['bottom'],
        ]

        self.assertTrue(all(side == bottom_center for side in bottom_face))
        
        # all 'sides' match their corresponding center
        self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], front_center)
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['front'], front_center)
        self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], front_center)

        self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], left_center)
        self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], left_center)
        self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], left_center)

        self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], back_center)
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['back'], back_center)
        self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], back_center)

        self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], right_center)
        self.assertEqual(self.cube.bot_layer['right_middle'].sides['right'], right_center)
        self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], right_center)

    def test_middle_layer(self):

        self.cube._solve_mid_layer()

        front_center = self.cube.mid_layer['front_center'].sides['front']
        left_center = self.cube.mid_layer['left_center'].sides['left']
        right_center = self.cube.mid_layer['right_center'].sides['right']
        back_center = self.cube.mid_layer['back_center'].sides['back']

        self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], front_center)
        self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], front_center)

        self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], left_center)
        self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], left_center)

        self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], back_center)
        self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], back_center)

        self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], right_center)
        self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], right_center)

if __name__ == '__main__':
    unittest.main()