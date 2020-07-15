import unittest
from cube import RubiksCube


# rename that class
class CubeSolutionTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

# test solution funcs <- make sure the tests arent interfering with each other

    def bottom_face_tester(self):
        self.assertTrue(all(self.cube.bot_layer[bottom].sides['bottom'] for bottom in self.cube.bot_layer))

    def bottom_layer_tester(self):
        right_center = self.cube.mid_layer['right_center'].sides['right']
        left_center = self.cube.mid_layer['left_center'].sides['left']
        front_center = self.cube.mid_layer['front_center'].sides['front']
        back_center = self.cube.mid_layer['back_center'].sides['back']

        self.assertTrue(all(self.cube.bot_layer[bottom].sides['bottom'] for bottom in self.cube.bot_layer))
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
    
    def middle_layer_tester(self):
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
        self.cube._solve_bot_layer()
        self.bottom_layer_tester()

    def test_bottom_layer_robustness(self, n=50):

        for _ in range(n):
            self.cube.initialize_cube()
            self.test_bottom_layer()
            print("Success")
    
    def test_middle_layer(self):

        self.cube._solve_mid_layer()
        self.bottom_layer_tester()
        self.middle_layer_tester()

    
    def test_middle_layer_robustness(self, n=50):
        for _ in range(n):
            self.cube.initialize_cube()
            self.cube._solve_mid_layer()


    def test_top_cross(self):
        self.cube._solve_top_cross()

        self.bottom_layer_tester()
        self.middle_layer_tester()

        self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], 'y')
        self.assertEqual(self.cube.top_layer['front_middle'].sides['top'], 'y')
        self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], 'y')
        self.assertEqual(self.cube.top_layer['back_middle'].sides['top'], 'y')
    
    def test_top_cross_robustness(self, n=50):
        for _ in range(n):
            self.cube.initialize_cube()
            self.test_top_cross()


    def test_top_face(self):

        self.cube._solve_top_face()

        self.bottom_layer_tester()
        self.middle_layer_tester()

        self.assertTrue(all(self.cube.top_layer[top].sides['top'] for top in self.cube.top_layer))
    
    def test_top_face_robustness(self, n=50):
        for _ in range(n):
            self.cube.initialize_cube()
            self.test_top_face()
    
    def test_top_corners(self):

        self.cube._solve_top_corners()

        self.bottom_layer_tester()
        self.middle_layer_tester()

        # test all four corners match their centers.
        # front
        front_center = self.cube.mid_layer['front_center'].sides['front']
        self.assertEqual(self.cube.top_layer['front_right'].sides['front'], front_center)
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], front_center)

        # left
        left_center = self.cube.mid_layer['left_center'].sides['left']
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], left_center)
        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], left_center)

        # back
        back_center = self.cube.mid_layer['back_center'].sides['back']
        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], back_center)
        self.assertEqual(self.cube.top_layer['back_right'].sides['back'], back_center)

        # right
        right_center = self.cube.mid_layer['right_center'].sides['right']
        self.assertEqual(self.cube.top_layer['back_right'].sides['right'], right_center)
        self.assertEqual(self.cube.top_layer['front_right'].sides['right'], right_center)


    # def test_solved_cube(self):

    #     self.cube.solve_cube()

    #     top_center = self.cube.top_layer['top_center'].sides['top']
    #     bottom_center = self.cube.bot_layer['bottom_center'].sides['bottom']
    #     front_center = self.cube.mid_layer['front_center'].sides['front']
    #     back_center = self.cube.mid_layer['back_center'].sides['back']
    #     right_center = self.cube.mid_layer['right_center'].sides['right']
    #     left_center = self.cube.mid_layer['left_center'].sides['left']

    #     # top face
    #     self.assertEqual(self.cube.top_layer['front_right'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['front_left'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['front_middle'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['back_right'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['back_left'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], top_center)
    #     self.assertEqual(self.cube.top_layer['back_middle'].sides['top'], top_center)

    #     # bot face
    #     bottom_face = [
    #         self.cube.bot_layer['front_right'].sides['bottom'],
    #         self.cube.bot_layer['front_middle'].sides['bottom'],
    #         self.cube.bot_layer['front_left'].sides['bottom'],
    #         self.cube.bot_layer['back_left'].sides['bottom'],
    #         self.cube.bot_layer['back_right'].sides['bottom'],
    #         self.cube.bot_layer['back_middle'].sides['bottom'],
    #         self.cube.bot_layer['left_middle'].sides['bottom'],
    #         self.cube.bot_layer['right_middle'].sides['bottom'],
    #     ]

    #     self.assertTrue(all(side == bottom_center for side in bottom_face))

    #     # front face
    #     self.assertEqual(self.cube.top_layer['front_right'].sides['front'], front_center)
    #     self.assertEqual(self.cube.top_layer['front_middle'].sides['front'], front_center)
    #     self.assertEqual(self.cube.top_layer['front_left'].sides['front'], front_center)
    #     self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], front_center)
    #     self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], front_center)
    #     self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], front_center)
    #     self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], front_center)
    #     self.assertEqual(self.cube.bot_layer['front_middle'].sides['front'], front_center)

    #     # back face
    #     self.assertEqual(self.cube.top_layer['back_right'].sides['back'], back_center)
    #     self.assertEqual(self.cube.top_layer['back_left'].sides['back'], back_center)
    #     self.assertEqual(self.cube.top_layer['back_middle'].sides['back'], back_center)
    #     self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], back_center)
    #     self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], back_center)
    #     self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], back_center)
    #     self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], back_center)
    #     self.assertEqual(self.cube.bot_layer['back_middle'].sides['back'], back_center)

    #     # right face
    #     self.assertEqual(self.cube.top_layer['front_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.top_layer['back_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.top_layer['right_middle'].sides['right'], right_center)
    #     self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], right_center)
    #     self.assertEqual(self.cube.bot_layer['right_middle'].sides['right'], right_center)

    #     # left face
    #     self.assertEqual(self.cube.top_layer['front_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.top_layer['back_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.top_layer['left_middle'].sides['left'], left_center)
    #     self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], left_center)
    #     self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], left_center)

        



if __name__ == '__main__':
    unittest.main()