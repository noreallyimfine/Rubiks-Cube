import unittest
from cube import RubiksCube

class CubeSetupTests(unittest.TestCase):
    def setUp(self):
        self.cube = RubiksCube()

    def test_color_count(self):

        # make sure there are 9 of each color
        color_dict = {'r': 0, 'o': 0, 'g': 0, 'b': 0, 'y': 0, 'w': 0}

        pieces = [
            self.cube.top_layer['front_right'],
            self.cube.top_layer['back_right'],
            self.cube.top_layer['front_left'],
            self.cube.top_layer['back_left'],
            self.cube.top_layer['back_middle'],
            self.cube.top_layer['front_middle'],
            self.cube.top_layer['right_middle'],
            self.cube.top_layer['left_middle'],
            self.cube.top_layer['top_center'],
            self.cube.mid_layer['left_center'],
            self.cube.mid_layer['right_center'],
            self.cube.mid_layer['front_center'],
            self.cube.mid_layer['back_center'],
            self.cube.mid_layer['front_left'],
            self.cube.mid_layer['back_left'],
            self.cube.mid_layer['back_right'],
            self.cube.mid_layer['front_right'],
            self.cube.bot_layer['front_right'],
            self.cube.bot_layer['front_left'],
            self.cube.bot_layer['back_left'],
            self.cube.bot_layer['back_right'],
            self.cube.bot_layer['back_middle'],
            self.cube.bot_layer['front_middle'],
            self.cube.bot_layer['right_middle'],
            self.cube.bot_layer['left_middle'],
            self.cube.bot_layer['bottom_center'],
        ]

        self.assertEqual(len(pieces), 26)


        for piece in pieces:
            for side in piece.sides:
                color = piece.sides[side]
                color_dict[color] += 1

        for color in color_dict:
            self.assertEqual(color_dict[color], 9)
    
    def test_centers(self):

        top_bottom = (self.cube.top_layer['top_center'].sides['top'], self.cube.bot_layer['bottom_center'].sides['bottom'])
        right_left = (self.cube.mid_layer['right_center'].sides['right'], self.cube.mid_layer['left_center'].sides['left'])
        front_back = (self.cube.mid_layer['front_center'].sides['front'], self.cube.mid_layer['back_center'].sides['back'])
        self.assertIn(top_bottom, self.cube.opposing_colors)
        self.assertIn(right_left, self.cube.opposing_colors)
        self.assertIn(front_back, self.cube.opposing_colors)
        
    def test_opposing_colors(self):

        # check that no combo of colors on any piece is opposing colors
        # if the piece is an edge, just need to compare the two sides
        for piece in self.cube.edges:
            sides_tuple = tuple(piece.sides.values())

            self.assertNotIn(sides_tuple, self.cube.opposing_colors)
        # if its a corner, need to compare a:b, a:c, b:c
        for corner in self.cube.corners:
            sides_tuple = tuple(corner.sides.values())

            self.assertNotIn((sides_tuple[0], sides_tuple[1]), self.cube.opposing_colors)
            self.assertNotIn((sides_tuple[0], sides_tuple[2]), self.cube.opposing_colors)
            self.assertNotIn((sides_tuple[1], sides_tuple[2]), self.cube.opposing_colors)
        
    
    def test_piece_colors(self):

        # Test the each color combo is hit the right amount of times

        # there should be 12 edges
        # top + 4 sides = 4
        # bottom + 4 sides = 4
        # front + 2 sides = 2
        # back + 2 sides = 2
        # color combos should be [(top, left), (top, right),
        #                         (top, front), (top, back),
        #                         (bottom, left), (bottom, right),
        #                         (bottom, front), (bottom, back),
        #                         (front, left), (front, right),
        #                         (back, left), (back, right)]

        # theres 8 corners
        # top + front + 2 sides = 2
        # top + back + 2 sides = 2
        # bottom + front + 2 sides = 2
        # bottom + back + 2 sides = 2

        # color combos should be [(top, front, left), (top, front, right),
        #                         (bottom, front, left), (bottom, front, right),
        #                         (top, back, left), (top, back, right),
        #                         (bottom, back, left), (bottom, back, right)]
        pass



if __name__ == "__main__":
    unittest.main()