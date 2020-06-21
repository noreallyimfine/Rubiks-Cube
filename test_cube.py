import unittest
from cube import RubiksCube

class CubeTurnTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_L(self):

        # Corners
        top_back_left = self.cube.top_layer['back_left'].sides.copy()
        top_front_left = self.cube.top_layer['front_left'].sides.copy()
        bot_front_left = self.cube.bot_layer['front_left'].sides.copy()
        bot_back_left = self.cube.bot_layer['back_left'].sides.copy()

        # Edges
        mid_back_left = self.cube.mid_layer['back_left'].sides.copy()
        top_left_middle = self.cube.top_layer['left_middle'].sides.copy()
        mid_front_left = self.cube.mid_layer['front_left'].sides.copy()
        bot_left_middle = self.cube.bot_layer['left_middle'].sides.copy()


        self.cube._L()

        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], top_front_left['top'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], top_front_left['front'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], top_front_left['left'])

        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], bot_front_left['left'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], bot_front_left['bottom'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['top'], bot_front_left['front'])

        self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], bot_back_left['left'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], bot_back_left['bottom'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['bottom'], bot_back_left['back'])

        self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], top_back_left['left'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], top_back_left['top'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['bottom'], top_back_left['back'])

        self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], top_left_middle['left'])
        self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], top_left_middle['top'])

        self.assertEqual(self.cube.top_layer['left_middle'].sides['left'], mid_front_left['left'])
        self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], mid_front_left['front'])

        self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], bot_left_middle['left'])
        self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], bot_left_middle['bottom'])

        self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], mid_back_left['left'])
        self.assertEqual(self.cube.bot_layer['left_middle'].sides['bottom'], mid_back_left['back'])

    def test_L_prime(self):

        # Corners
        top_back_left = self.cube.top_layer['back_left'].sides.copy()
        top_front_left = self.cube.top_layer['front_left'].sides.copy()
        bot_front_left = self.cube.bot_layer['front_left'].sides.copy()
        bot_back_left = self.cube.bot_layer['back_left'].sides.copy()

        # Edges
        mid_back_left = self.cube.mid_layer['back_left'].sides.copy()
        top_left_middle = self.cube.top_layer['left_middle'].sides.copy()
        mid_front_left = self.cube.mid_layer['front_left'].sides.copy()
        bot_left_middle = self.cube.bot_layer['left_middle'].sides.copy()


        self.cube._L_prime()

        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], bot_back_left['bottom'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], bot_back_left['back'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], bot_back_left['left'])

        self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], bot_front_left['left'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['bottom'], bot_front_left['front'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], bot_front_left['bottom'])

        self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], top_front_left['left'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], top_front_left['top'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['bottom'], top_front_left['front'])

        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], top_back_left['left'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['top'], top_back_left['back'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], top_back_left['top'])

        self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], mid_front_left['left'])
        self.assertEqual(self.cube.bot_layer['left_middle'].sides['bottom'], mid_front_left['front'])

        self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], top_left_middle['left'])
        self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], top_left_middle['top'])

        self.assertEqual(self.cube.top_layer['left_middle'].sides['left'], mid_back_left['left'])
        self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], mid_back_left['back'])

        self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], bot_left_middle['left'])
        self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], bot_left_middle['bottom'])

    def test_R(self):

        # Corners
        top_back_right = self.cube.top_layer['back_right'].sides.copy()
        top_front_right = self.cube.top_layer['front_right'].sides.copy()
        bot_front_right = self.cube.bot_layer['front_right'].sides.copy()
        bot_back_right = self.cube.bot_layer['back_right'].sides.copy()

        # Edges
        mid_back_right = self.cube.mid_layer['back_right'].sides.copy()
        top_right_middle = self.cube.top_layer['right_middle'].sides.copy()
        mid_front_right = self.cube.mid_layer['front_right'].sides.copy()
        bot_right_middle = self.cube.bot_layer['right_middle'].sides.copy()


        self.cube._R()

        self.assertEqual(self.cube.top_layer['back_right'].sides['top'], top_front_right['front'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['back'], top_front_right['top'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['right'], top_front_right['right'])

        self.assertEqual(self.cube.top_layer['front_right'].sides['front'], bot_front_right['bottom'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['top'], bot_front_right['front'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['right'], bot_front_right['right'])

        self.assertEqual(self.cube.bot_layer['front_right'].sides['bottom'], bot_back_right['back'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], bot_back_right['bottom'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], bot_back_right['right'])

        self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], top_back_right['top'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['bottom'], top_back_right['back'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], top_back_right['right'])

        self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], mid_front_right['front'])
        self.assertEqual(self.cube.top_layer['right_middle'].sides['right'], mid_front_right['right'])

        self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], bot_right_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], bot_right_middle['right'])

        self.assertEqual(self.cube.bot_layer['right_middle'].sides['bottom'], mid_back_right['back'])
        self.assertEqual(self.cube.bot_layer['right_middle'].sides['right'], mid_back_right['right'])

        self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], top_right_middle['top'])
        self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], top_right_middle['right'])

    def test_R_prime(self):

        # Corners
        top_back_right = self.cube.top_layer['back_right'].sides.copy()
        top_front_right = self.cube.top_layer['front_right'].sides.copy()
        bot_front_right = self.cube.bot_layer['front_right'].sides.copy()
        bot_back_right = self.cube.bot_layer['back_right'].sides.copy()

        # Edges
        mid_back_right = self.cube.mid_layer['back_right'].sides.copy()
        top_right_middle = self.cube.top_layer['right_middle'].sides.copy()
        mid_front_right = self.cube.mid_layer['front_right'].sides.copy()
        bot_right_middle = self.cube.bot_layer['right_middle'].sides.copy()


        self.cube._R_prime()

        self.assertEqual(self.cube.top_layer['back_right'].sides['top'], bot_back_right['back'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['back'], bot_back_right['bottom'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['right'], bot_back_right['right'])

        self.assertEqual(self.cube.bot_layer['back_right'].sides['bottom'], bot_front_right['front'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], bot_front_right['bottom'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], bot_front_right['right'])

        self.assertEqual(self.cube.bot_layer['front_right'].sides['bottom'], top_front_right['front'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], top_front_right['top'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], top_front_right['right'])

        self.assertEqual(self.cube.top_layer['front_right'].sides['top'], top_back_right['back'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['front'], top_back_right['top'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['right'], top_back_right['right'])

        self.assertEqual(self.cube.top_layer['right_middle'].sides['top'], mid_back_right['back'])
        self.assertEqual(self.cube.top_layer['right_middle'].sides['right'], mid_back_right['right'])

        self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], bot_right_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], bot_right_middle['right'])

        self.assertEqual(self.cube.bot_layer['right_middle'].sides['bottom'], mid_front_right['front'])
        self.assertEqual(self.cube.bot_layer['right_middle'].sides['right'], mid_front_right['right'])

        self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], top_right_middle['top'])
        self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], top_right_middle['right'])

    def test_F(self):

        top_front_right = self.cube.top_layer['front_right'].sides.copy()
        top_front_left = self.cube.top_layer['front_left'].sides.copy()
        bot_front_left = self.cube.bot_layer['front_left'].sides.copy()
        bot_front_right = self.cube.bot_layer['front_right'].sides.copy()

        top_front_middle = self.cube.top_layer['front_middle'].sides.copy()
        mid_front_left = self.cube.mid_layer['front_left'].sides.copy()
        bot_front_middle = self.cube.bot_layer['front_middle'].sides.copy()
        mid_front_right = self.cube.mid_layer['front_right'].sides.copy()

        self.cube._F()

        self.assertEqual(self.cube.top_layer['front_right'].sides['right'], top_front_left['top'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['top'], top_front_left['left'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['front'], top_front_left['front'])

        self.assertEqual(self.cube.top_layer['front_left'].sides['top'], bot_front_left['left'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], bot_front_left['bottom'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], bot_front_left['front'])

        self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], bot_front_right['bottom'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['bottom'], bot_front_right['right'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], bot_front_right['front'])

        self.assertEqual(self.cube.bot_layer['front_right'].sides['bottom'], top_front_right['right'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], top_front_right['top'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], top_front_right['front'])

        self.assertEqual(self.cube.top_layer['front_middle'].sides['top'], mid_front_left['left'])
        self.assertEqual(self.cube.top_layer['front_middle'].sides['front'], mid_front_left['front'])

        self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], bot_front_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], bot_front_middle['front'])

        self.assertEqual(self.cube.bot_layer['front_middle'].sides['bottom'], mid_front_right['right'])
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['front'], mid_front_right['front'])

        self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], top_front_middle['top'])
        self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], top_front_middle['front'])

    def test_F_prime(self):

        top_front_right = self.cube.top_layer['front_right'].sides.copy()
        top_front_left = self.cube.top_layer['front_left'].sides.copy()
        bot_front_left = self.cube.bot_layer['front_left'].sides.copy()
        bot_front_right = self.cube.bot_layer['front_right'].sides.copy()

        top_front_middle = self.cube.top_layer['front_middle'].sides.copy()
        mid_front_left = self.cube.mid_layer['front_left'].sides.copy()
        bot_front_middle = self.cube.bot_layer['front_middle'].sides.copy()
        mid_front_right = self.cube.mid_layer['front_right'].sides.copy()

        self.cube._F_prime()

        self.assertEqual(self.cube.top_layer['front_left'].sides['left'], top_front_right['top'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['top'], top_front_right['right'])
        self.assertEqual(self.cube.top_layer['front_left'].sides['front'], top_front_right['front'])

        self.assertEqual(self.cube.top_layer['front_right'].sides['top'], bot_front_right['right'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['right'], bot_front_right['bottom'])
        self.assertEqual(self.cube.top_layer['front_right'].sides['front'], bot_front_right['front'])

        self.assertEqual(self.cube.bot_layer['front_right'].sides['bottom'], bot_front_left['left'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['right'], bot_front_left['bottom'])
        self.assertEqual(self.cube.bot_layer['front_right'].sides['front'], bot_front_left['front'])

        self.assertEqual(self.cube.bot_layer['front_left'].sides['bottom'], top_front_left['left'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['left'], top_front_left['top'])
        self.assertEqual(self.cube.bot_layer['front_left'].sides['front'], top_front_left['front'])

        self.assertEqual(self.cube.top_layer['front_middle'].sides['top'], mid_front_right['right'])
        self.assertEqual(self.cube.top_layer['front_middle'].sides['front'], mid_front_right['front'])

        self.assertEqual(self.cube.mid_layer['front_right'].sides['right'], bot_front_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['front_right'].sides['front'], bot_front_middle['front'])

        self.assertEqual(self.cube.bot_layer['front_middle'].sides['bottom'], mid_front_left['left'])
        self.assertEqual(self.cube.bot_layer['front_middle'].sides['front'], mid_front_left['front'])

        self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], top_front_middle['top'])
        self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], top_front_middle['front'])

    def test_B(self):

        top_back_right = self.cube.top_layer['back_right'].sides.copy()
        bot_back_right = self.cube.bot_layer['back_right'].sides.copy()
        bot_back_left = self.cube.bot_layer['back_left'].sides.copy()
        top_back_left = self.cube.top_layer['back_left'].sides.copy()

        top_back_middle = self.cube.top_layer['back_middle'].sides.copy()
        mid_back_right = self.cube.mid_layer['back_right'].sides.copy()
        bot_back_middle = self.cube.bot_layer['back_middle'].sides.copy()
        mid_back_left = self.cube.mid_layer['back_left'].sides.copy()

        self.cube._B()

        self.assertEqual(self.cube.top_layer['back_right'].sides['top'], bot_back_right['right'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['right'], bot_back_right['bottom'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['back'], bot_back_right['back'])

        self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], bot_back_left['bottom'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['bottom'], bot_back_left['left'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], bot_back_left['back'])

        self.assertEqual(self.cube.bot_layer['back_left'].sides['bottom'], top_back_left['left'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], top_back_left['top'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], top_back_left['back'])

        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], top_back_right['top'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], top_back_right['right'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], top_back_right['back'])

        self.assertEqual(self.cube.top_layer['back_middle'].sides['top'], mid_back_right['right'])
        self.assertEqual(self.cube.top_layer['back_middle'].sides['back'], mid_back_right['back'])

        self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], bot_back_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], bot_back_middle['back'])
        
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['bottom'], mid_back_left['left'])
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['back'], mid_back_left['back'])

        self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], top_back_middle['top'])
        self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], top_back_middle['back'])

    def test_B_prime(self):

        top_back_right = self.cube.top_layer['back_right'].sides.copy()
        bot_back_right = self.cube.bot_layer['back_right'].sides.copy()
        bot_back_left = self.cube.bot_layer['back_left'].sides.copy()
        top_back_left = self.cube.top_layer['back_left'].sides.copy()

        top_back_middle = self.cube.top_layer['back_middle'].sides.copy()
        mid_back_right = self.cube.mid_layer['back_right'].sides.copy()
        bot_back_middle = self.cube.bot_layer['back_middle'].sides.copy()
        mid_back_left = self.cube.mid_layer['back_left'].sides.copy()

        self.cube._B_prime()

        self.assertEqual(self.cube.top_layer['back_right'].sides['right'], top_back_left['top'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['top'], top_back_left['left'])
        self.assertEqual(self.cube.top_layer['back_right'].sides['back'], top_back_left['back'])

        self.assertEqual(self.cube.top_layer['back_left'].sides['top'], bot_back_left['left'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['left'], bot_back_left['bottom'])
        self.assertEqual(self.cube.top_layer['back_left'].sides['back'], bot_back_left['back'])

        self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], bot_back_right['bottom'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['bottom'], bot_back_right['right'])
        self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], bot_back_right['back'])

        self.assertEqual(self.cube.bot_layer['back_right'].sides['bottom'], top_back_right['right'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['right'], top_back_right['top'])
        self.assertEqual(self.cube.bot_layer['back_right'].sides['back'], top_back_right['back'])

        self.assertEqual(self.cube.top_layer['back_middle'].sides['top'], mid_back_left['left'])
        self.assertEqual(self.cube.top_layer['back_middle'].sides['back'], mid_back_left['back'])

        self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], bot_back_middle['bottom'])
        self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], bot_back_middle['back'])

        self.assertEqual(self.cube.bot_layer['back_middle'].sides['bottom'], mid_back_right['right'])
        self.assertEqual(self.cube.bot_layer['back_middle'].sides['back'], mid_back_right['back'])

        self.assertEqual(self.cube.mid_layer['back_right'].sides['right'], top_back_middle['top'])
        self.assertEqual(self.cube.mid_layer['back_right'].sides['back'], top_back_middle['back'])

    def test_U(self):

        top_front_right = self.cube.top_layer['front_right'].sides.copy()
        top_back_right = self.cube.top_layer['back_right'].sides.copy()
        top_back_left = self.cube.top_layer['back_left'].sides.copy()
        top_back_right = self.cube.top_layer['back_right'].sides.copy()

        top_front_middle = self.cube.top_layer['front_middle'].sides.copy()
        top_right_middle = self.cube.top_layer['right_middle'].sides.copy()
        top_back_middle = self.cube.top_layer['back_middle'].sides.copy()
        top_left_middle = self.cube.top_layer['left_middle'].sides.copy()




if __name__ == "__main__":
    unittest.main()