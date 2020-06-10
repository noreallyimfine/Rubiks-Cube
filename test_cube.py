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

        # self.assertEqual(self.cube.bot_layer['back_left'].sides['left'], top_back_left['left'])
        # self.assertEqual(self.cube.bot_layer['back_left'].sides['back'], top_back_left['top'])
        # self.assertEqual(self.cube.bot_layer['back_left'].sides['bottom'], top_back_left['back'])

        # self.assertEqual(self.cube.mid_layer['back_left'].sides['left'], top_left_middle['left'])
        # self.assertEqual(self.cube.mid_layer['back_left'].sides['back'], top_left_middle['top'])

        # self.assertEqual(self.cube.top_layer['left_middle'].sides['left'], mid_front_left['left'])
        # self.assertEqual(self.cube.top_layer['left_middle'].sides['top'], mid_front_left['front'])

        # self.assertEqual(self.cube.mid_layer['front_left'].sides['left'], bot_left_middle['left'])
        # self.assertEqual(self.cube.mid_layer['front_left'].sides['front'], bot_left_middle['bottom'])

        # self.assertEqual(self.cube.bot_layer['left_middle'].sides['left'], mid_back_left['left'])
        # self.assertEqual(self.cube.bot_layer['left_middle'].sides['bottom'], mid_back_left['back'])


if __name__ == "__main__":
    unittest.main()