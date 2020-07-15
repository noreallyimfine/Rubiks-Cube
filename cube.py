'''
Class instantiation of a Rubik's Cube, with the logic to solve it.
'''

import random
from piece import Piece, Center, Edge, Corner

class RubiksCube:

    colors = ['w', 'y', 'o', 'b', 'r', 'g']
    verticals = ['front', 'back']
    horizontals = ['right', 'left']
    
    def __init__(self):
        self.bot_layer = {'bottom_center': Center(sides=['bottom']), 
                          'front_middle': Edge(sides=['front', 'bottom']),
                          'front_left': Corner(sides=['front', 'bottom', 'left']),
                          'front_right': Corner(sides=['front', 'bottom', 'right']),
                          'back_left': Corner(sides=['back', 'bottom', 'left']),
                          'back_right': Corner(sides=['back', 'bottom', 'right']),
                          'back_middle': Edge(sides=['back', 'bottom']),
                          'left_middle': Edge(sides=['left', 'bottom']),
                          'right_middle': Edge(sides=['right', 'bottom'])}
        self.mid_layer = {'front_center': Center(sides=['front']),
                          'right_center': Center(sides=['right']),
                          'left_center': Center(sides=['left']),
                          'back_center': Center(sides=['back']),
                          'front_left': Edge(sides=['front', 'left']),
                          'front_right': Edge(sides=['front', 'right']),
                          'back_left': Edge(sides=['back', 'left']),
                          'back_right': Edge(sides=['back', 'right'])}
        self.top_layer = {'top_center': Center(sides=['top']),
                          'front_middle': Edge(sides=['front', 'top']),
                          'front_left': Corner(sides=['top', 'front', 'left']),
                          'front_right': Corner(sides=['top', 'front', 'right']),
                          'back_left': Corner(sides=['top', 'back', 'left']),
                          'back_right': Corner(sides=['top', 'back', 'right']),
                          'back_middle': Edge(sides=['back', 'top']),
                          'left_middle': Edge(sides=['left', 'top']),
                          'right_middle': Edge(sides=['right', 'top'])}
        
        self.centers = [self.bot_layer['bottom_center'],
                        self.mid_layer['right_center'],
                        self.mid_layer['left_center'],
                        self.mid_layer['front_center'],
                        self.mid_layer['back_center'],
                        self.top_layer['top_center']]

        self.edges = [self.bot_layer['front_middle'],
                      self.bot_layer['back_middle'],
                      self.bot_layer['left_middle'],
                      self.bot_layer['right_middle'],
                      self.mid_layer['front_left'],
                      self.mid_layer['front_right'],
                      self.mid_layer['back_left'],
                      self.mid_layer['back_right'],
                      self.top_layer['front_middle'],
                      self.top_layer['back_middle'],
                      self.top_layer['left_middle'],
                      self.top_layer['right_middle']]

        self.corners = [self.bot_layer['front_left'],
                        self.bot_layer['back_left'],
                        self.bot_layer['front_right'],
                        self.bot_layer['back_right'],
                        self.top_layer['front_left'],
                        self.top_layer['back_left'], 
                        self.top_layer['front_right'],
                        self.top_layer['back_right']]
        
        self.opposing_colors = [('w', 'y'), ('r', 'o'), ('g', 'b')]

        # Automatically initialize cube upon instantiation
        self.initialize_cube()
    
    def __repr__(self):
        return f"""RubiksCube({self.top_layer}, {self.mid_layer}, {self.bot_layer})"""

    def __str__(self):
        output = f"""
        Top layer: {self.top_layer}\n\n\n
        Middle layer: {self.mid_layer}\n\n\n
        Bottom layer: {self.bot_layer}\n\n\n"""
        return output

    def print_cube(self):

        # top face

        # front face

        # left face

        # back face

        # right face

        # bottom face
        pass
    def initialize_cube(self):
        '''
        Function to create the solvable cube, scrambled.
        First creates a comppleted cube, then scrambles it.
        '''
    
        # initialize a solved cube

        # top face - y
        self.top_layer['top_center'].sides['top'] = 'y'
        self.top_layer['front_right'].sides['top'] = 'y'
        self.top_layer['front_left'].sides['top'] = 'y'
        self.top_layer['front_middle'].sides['top'] = 'y'
        self.top_layer['left_middle'].sides['top'] = 'y'
        self.top_layer['right_middle'].sides['top'] = 'y'
        self.top_layer['back_middle'].sides['top'] = 'y'
        self.top_layer['back_left'].sides['top'] = 'y'
        self.top_layer['back_right'].sides['top'] = 'y'

        # bottom face - w
        self.bot_layer['bottom_center'].sides['bottom'] = 'w'
        self.bot_layer['front_right'].sides['bottom'] = 'w'
        self.bot_layer['front_left'].sides['bottom'] = 'w'
        self.bot_layer['front_middle'].sides['bottom'] = 'w'
        self.bot_layer['right_middle'].sides['bottom'] = 'w'
        self.bot_layer['left_middle'].sides['bottom'] = 'w'
        self.bot_layer['back_middle'].sides['bottom'] = 'w'
        self.bot_layer['back_right'].sides['bottom'] = 'w'
        self.bot_layer['back_left'].sides['bottom'] = 'w'

        # front face - r
        self.mid_layer['front_center'].sides['front'] = 'r'
        self.mid_layer['front_right'].sides['front'] = 'r'
        self.mid_layer['front_left'].sides['front'] = 'r'
        self.top_layer['front_left'].sides['front'] = 'r'
        self.top_layer['front_right'].sides['front'] = 'r'
        self.top_layer['front_middle'].sides['front'] = 'r'
        self.bot_layer['front_middle'].sides['front'] = 'r'
        self.bot_layer['front_right'].sides['front'] = 'r'
        self.bot_layer['front_left'].sides['front'] = 'r'

        # back face - o
        self.mid_layer['back_center'].sides['back'] = 'o'
        self.mid_layer['back_right'].sides['back'] = 'o'
        self.mid_layer['back_left'].sides['back'] = 'o'
        self.top_layer['back_left'].sides['back'] = 'o'
        self.top_layer['back_right'].sides['back'] = 'o'
        self.top_layer['back_middle'].sides['back'] = 'o'
        self.bot_layer['back_middle'].sides['back'] = 'o'
        self.bot_layer['back_left'].sides['back'] = 'o'
        self.bot_layer['back_right'].sides['back'] = 'o'

        # right face - g
        self.mid_layer['right_center'].sides['right'] = 'g'
        self.mid_layer['front_right'].sides['right'] = 'g'
        self.mid_layer['back_right'].sides['right'] = 'g'
        self.top_layer['back_right'].sides['right'] = 'g'
        self.top_layer['front_right'].sides['right'] = 'g'
        self.top_layer['right_middle'].sides['right'] = 'g'
        self.bot_layer['right_middle'].sides['right'] = 'g'
        self.bot_layer['back_right'].sides['right'] = 'g'
        self.bot_layer['front_right'].sides['right'] = 'g'

        # left face - b
        self.mid_layer['left_center'].sides['left'] = 'b'
        self.mid_layer['front_left'].sides['left'] = 'b'
        self.mid_layer['back_left'].sides['left'] = 'b'
        self.top_layer['back_left'].sides['left'] = 'b'
        self.top_layer['front_left'].sides['left'] = 'b'
        self.top_layer['left_middle'].sides['left'] = 'b'
        self.bot_layer['left_middle'].sides['left'] = 'b'
        self.bot_layer['front_left'].sides['left'] = 'b'
        self.bot_layer['back_left'].sides['left'] = 'b'

        self.scramble_cube()

    def scramble_cube(self):

        '''
        Scrambles cube by making 50 random turns
        '''

        # This could be better if i find some computer generated scrambles
        # can have list of scramble sequences
        # and randomly choose which one to use each time

        moves = [
            self._L,
            self._L_prime,
            self._R,
            self._R_prime,
            self._D,
            self._D_prime,
            self._U,
            self._U_prime,
            self._B,
            self._B_prime,
            self._F,
            self._F_prime
        ]

        # fewer turns for testing where mistakes are happening
        for _ in range(50):
            random.choice(moves)()
        # for _ in range(50):
        #     random.choice(moves)()
        

        # scramble the cube.
    def _L_prime(self):
        '''
        Turn left face counter-clockwise
        '''

        print("initiating L_prime turn")
        # CORNERS #

        # Temp variables so as not to overwrite as we go
        corner_a = self.top_layer['back_left'].sides['back']
        corner_b = self.top_layer['back_left'].sides['top']
        corner_c = self.top_layer['back_left'].sides['left']

        # Top back left <- Top front left
            # back <- top, top <- front, left <- left
        self.top_layer['back_left'].sides['back'] = self.top_layer['front_left'].sides['top']
        self.top_layer['back_left'].sides['top'] = self.top_layer['front_left'].sides['front']
        self.top_layer['back_left'].sides['left'] = self.top_layer['front_left'].sides['left']

        # Top front left <- Bot front left
            # top <- front, front <- bottom, left <- left
        self.top_layer['front_left'].sides['top'] = self.bot_layer['front_left'].sides['front']
        self.top_layer['front_left'].sides['front'] = self.bot_layer['front_left'].sides['bottom']
        self.top_layer['front_left'].sides['left'] = self.bot_layer['front_left'].sides['left']
        
        # Bot front left <- Bot back left
            # front <- bottom, bottom <- back, left <- left
        self.bot_layer['front_left'].sides['front'] = self.bot_layer['back_left'].sides['bottom']
        self.bot_layer['front_left'].sides['bottom'] = self.bot_layer['back_left'].sides['back']
        self.bot_layer['front_left'].sides['left'] = self.bot_layer['back_left'].sides['left']
        
        # Bot back left <- Top back left
            # bottom <- back, back <- top, left <- left
        self.bot_layer['back_left'].sides['bottom'] = corner_a
        self.bot_layer['back_left'].sides['back'] = corner_b
        self.bot_layer['back_left'].sides['left'] = corner_c
        
        # EDGES #
        # Temp variables so as not to overwrite as we go
        edge_a = self.mid_layer['back_left'].sides['back']
        edge_b = self.mid_layer['back_left'].sides['left']

        # Mid back left <- Top left middle 
            # back <- top, left <- left
        self.mid_layer['back_left'].sides['back'] = self.top_layer['left_middle'].sides['top']
        self.mid_layer['back_left'].sides['left'] = self.top_layer['left_middle'].sides['left']
        
        # Top left middle <- Mid front left
            # top <- front, left <- left
        self.top_layer['left_middle'].sides['top'] = self.mid_layer['front_left'].sides['front']
        self.top_layer['left_middle'].sides['left'] = self.mid_layer['front_left'].sides['left']

        # Mid front left <- Bot left middle
            # front <- bottom, left <- left
        self.mid_layer['front_left'].sides['front'] = self.bot_layer['left_middle'].sides['bottom']
        self.mid_layer['front_left'].sides['left'] = self.bot_layer['left_middle'].sides['left']

        # Bot left middle <- Mid back left (temp)
            # bottom <- back, left <- left
        self.bot_layer['left_middle'].sides['bottom'] = edge_a
        self.bot_layer['left_middle'].sides['left'] = edge_b

    def _L(self):
        '''
        Turn left face clockwise
        '''
        print("initiating L turn")

        # CORNERS # 

        # Temp variables so we dont overwrite as we go
        corner_a = self.top_layer['back_left'].sides['top']
        corner_b = self.top_layer['back_left'].sides['back']
        corner_c = self.top_layer['back_left'].sides['left']

        # Top back left <- Bottom back left 
            # back <- bottom, top <- back, left <- left
        self.top_layer['back_left'].sides['top'] = self.bot_layer['back_left'].sides['back']
        self.top_layer['back_left'].sides['back'] = self.bot_layer['back_left'].sides['bottom']
        self.top_layer['back_left'].sides['left'] = self.bot_layer['back_left'].sides['left']

        # bottom back left <- Bottom front left 
            # front -> bottom, bottom -> back, left -> left
        self.bot_layer['back_left'].sides['bottom'] = self.bot_layer['front_left'].sides['front']
        self.bot_layer['back_left'].sides['back'] = self.bot_layer['front_left'].sides['bottom']
        self.bot_layer['back_left'].sides['left'] = self.bot_layer['front_left'].sides['left']

        # bottom front left <- Top front left 
            # front <- top, bottom <- front, left <- left
        self.bot_layer['front_left'].sides['front'] = self.top_layer['front_left'].sides['top']
        self.bot_layer['front_left'].sides['bottom'] = self.top_layer['front_left'].sides['front']
        self.bot_layer['front_left'].sides['left'] = self.top_layer['front_left'].sides['left']

        # top front left <- Top back left 
            # top <- back, front <- top, left <- left
        self.top_layer['front_left'].sides['front'] = corner_a 
        self.top_layer['front_left'].sides['top'] = corner_b 
        self.top_layer['front_left'].sides['left'] = corner_c 

        # EDGES #

        # Temp variables so one edge doesn't get overwritten as we go
        edge_a = self.bot_layer['left_middle'].sides['bottom']
        edge_b = self.bot_layer['left_middle'].sides['left']

        # bottom left mid <- Mid front left 
            # bottom <- front, left <- left
        self.bot_layer['left_middle'].sides['bottom'] = self.mid_layer['front_left'].sides['front']
        self.bot_layer['left_middle'].sides['left'] = self.mid_layer['front_left'].sides['left']

        #Mid front left <- Top left middle 
            # front <- top, left <- left
        self.mid_layer['front_left'].sides['front'] = self.top_layer['left_middle'].sides['top']
        self.mid_layer['front_left'].sides['left'] = self.top_layer['left_middle'].sides['left']

        # top left middle <- Mid back left 
            # top <- back, left <- left
        self.top_layer['left_middle'].sides['top'] = self.mid_layer['back_left'].sides['back']
        self.top_layer['left_middle'].sides['left'] = self.mid_layer['back_left'].sides['left']

        # Middle back left <- Bottom left middle 
            # back <- bottom, left <- left
        self.mid_layer['back_left'].sides['back'] = edge_a
        self.mid_layer['back_left'].sides['left'] = edge_b
    
    
    def _R(self):
        '''
        Turn right face clockwise
        '''

        print("initiating _R turn")

        # CORNERS # 

        # Temp variables to protect against overwriting
        corner_a = self.top_layer['back_right'].sides['top']
        corner_b = self.top_layer['back_right'].sides['back']
        corner_c = self.top_layer['back_right'].sides['right']

        # Top back right <- Top front right
            # top <- front, back <- top, right <- right
        self.top_layer['back_right'].sides['top'] = self.top_layer['front_right'].sides['front']
        self.top_layer['back_right'].sides['back'] = self.top_layer['front_right'].sides['top']
        self.top_layer['back_right'].sides['right'] = self.top_layer['front_right'].sides['right']
        
        # Top front right <- Bot front right
            # front <- bottom, top <- front, right <- right
        self.top_layer['front_right'].sides['front'] = self.bot_layer['front_right'].sides['bottom'] 
        self.top_layer['front_right'].sides['top'] = self.bot_layer['front_right'].sides['front'] 
        self.top_layer['front_right'].sides['right'] = self.bot_layer['front_right'].sides['right'] 
        
        
        # Bot front right <- Bot back right
            # front <- bottom, bottom <- back, right <- right
        self.bot_layer['front_right'].sides['bottom'] = self.bot_layer['back_right'].sides['back']
        self.bot_layer['front_right'].sides['front'] = self.bot_layer['back_right'].sides['bottom']
        self.bot_layer['front_right'].sides['right'] = self.bot_layer['back_right'].sides['right']
        
        # Bot back right <- Top back right (temp)
            # back <- top, bottom <- back, right <- right
        self.bot_layer['back_right'].sides['back'] = corner_a
        self.bot_layer['back_right'].sides['bottom'] = corner_b
        self.bot_layer['back_right'].sides['right'] = corner_c
        
        # EDGES #

        # Temp variables to protect against overwrite
        edge_a = self.top_layer['right_middle'].sides['top']
        edge_b = self.top_layer['right_middle'].sides['right']

        # Top right middle <- Mid front right
            # top <- front, right <- right
        self.top_layer['right_middle'].sides['top'] = self.mid_layer['front_right'].sides['front']
        self.top_layer['right_middle'].sides['right'] = self.mid_layer['front_right'].sides['right']

        # Mid front right <- Bot right middle
            # front <- bottom, right <- right
        self.mid_layer['front_right'].sides['front'] = self.bot_layer['right_middle'].sides['bottom']
        self.mid_layer['front_right'].sides['right'] = self.bot_layer['right_middle'].sides['right']

        # Bot right middle <- Mid back right
            # bottom <- back, right <- right
        self.bot_layer['right_middle'].sides['bottom'] = self.mid_layer['back_right'].sides['back']
        self.bot_layer['right_middle'].sides['right'] = self.mid_layer['back_right'].sides['right']

        # Mid back right <- Top right middle (temp)
            # back <- top, right <- right            
        self.mid_layer['back_right'].sides['back'] = edge_a
        self.mid_layer['back_right'].sides['right'] = edge_b

    
    def _R_prime(self):
        '''
        Turn right face counter-clockwise
        '''
        print("initiating _R_prime turn")

        # CORNERS #

        # temp variables to protect against overwriting
        corner_a = self.top_layer['back_right'].sides['top']
        corner_b = self.top_layer['back_right'].sides['back']
        corner_c = self.top_layer['back_right'].sides['right']

        # Top back right <- Bot back right
            # top <- back, back <- bottom, right <- right
        self.top_layer['back_right'].sides['top'] = self.bot_layer['back_right'].sides['back']
        self.top_layer['back_right'].sides['back'] = self.bot_layer['back_right'].sides['bottom']
        self.top_layer['back_right'].sides['right'] = self.bot_layer['back_right'].sides['right']

        # Bot back right <- Bot front right
            # back <- bottom, bottom <- front, right <- right
        self.bot_layer['back_right'].sides['back'] = self.bot_layer['front_right'].sides['bottom']
        self.bot_layer['back_right'].sides['bottom'] = self.bot_layer['front_right'].sides['front']
        self.bot_layer['back_right'].sides['right'] = self.bot_layer['front_right'].sides['right']
        
        # Bot front right <- Top front right
            # bottom <- front, front <- top, right <- right
        self.bot_layer['front_right'].sides['bottom'] = self.top_layer['front_right'].sides['front']
        self.bot_layer['front_right'].sides['front'] = self.top_layer['front_right'].sides['top']
        self.bot_layer['front_right'].sides['right'] = self.top_layer['front_right'].sides['right']

        # Top front right <- Top back right
            # front <- top, top <- back, right <- right
        self.top_layer['front_right'].sides['front'] = corner_a
        self.top_layer['front_right'].sides['top'] = corner_b
        self.top_layer['front_right'].sides['right'] = corner_c
        
        # EDGES
        
        # temp variables to protect against overwriting
        edge_a = self.top_layer['right_middle'].sides['top']
        edge_b = self.top_layer['right_middle'].sides['right']

        # Top right middle <- Mid back right
            # top <- back, right <- right
        self.top_layer['right_middle'].sides['top'] = self.mid_layer['back_right'].sides['back']
        self.top_layer['right_middle'].sides['right'] = self.mid_layer['back_right'].sides['right']
        
        # Mid back right <- Bot right middle
            # back <- bottom, right <- right
        self.mid_layer['back_right'].sides['back'] = self.bot_layer['right_middle'].sides['bottom']
        self.mid_layer['back_right'].sides['right'] = self.bot_layer['right_middle'].sides['right']
        
        # Bot right middle <- Mid front right
            # bottom <- front, right <- right
        self.bot_layer['right_middle'].sides['bottom'] = self.mid_layer['front_right'].sides['front']
        self.bot_layer['right_middle'].sides['right'] = self.mid_layer['front_right'].sides['right']

        # Mid front right <- Top right middle
            # front <- top, right <- right
        self.mid_layer['front_right'].sides['front'] = edge_a
        self.mid_layer['front_right'].sides['right'] = edge_b

    def _F(self):
        '''
        Turn front face clockwise
        '''
        print("initiating _F turn")

        # CORNERS #

        # Temp variables to protect against overwriting as we go
        corner_a = self.top_layer['front_right'].sides['right']
        corner_b = self.top_layer['front_right'].sides['top']
        corner_c = self.top_layer['front_right'].sides['front']

        # Top front right <- Top front left
            # right <- top, top <- left, front <- front
        self.top_layer['front_right'].sides['right'] = self.top_layer['front_left'].sides['top']
        self.top_layer['front_right'].sides['top'] = self.top_layer['front_left'].sides['left']
        self.top_layer['front_right'].sides['front'] = self.top_layer['front_left'].sides['front']
        
        # Top front left <- Bot front left
            # top <- left, left <- bottom, front <- front
        self.top_layer['front_left'].sides['top'] = self.bot_layer['front_left'].sides['left']
        self.top_layer['front_left'].sides['left'] = self.bot_layer['front_left'].sides['bottom']
        self.top_layer['front_left'].sides['front'] = self.bot_layer['front_left'].sides['front']

        # Bot front left <- Bot front right
            # left <- bottom, bottom <- right, front <- front
        self.bot_layer['front_left'].sides['left'] = self.bot_layer['front_right'].sides['bottom']
        self.bot_layer['front_left'].sides['bottom'] = self.bot_layer['front_right'].sides['right']
        self.bot_layer['front_left'].sides['front'] = self.bot_layer['front_right'].sides['front']

        # Bot front right <- Top front right (temp)
            # bottom <- right, right <- top, front <- front
        self.bot_layer['front_right'].sides['bottom'] = corner_a
        self.bot_layer['front_right'].sides['right'] = corner_b
        self.bot_layer['front_right'].sides['front'] = corner_c
        
        # EDGES #

        # Temp variables to protect against overwriting as we go
        edge_a = self.top_layer['front_middle'].sides['top']
        edge_b = self.top_layer['front_middle'].sides['front']
        
        # Top front middle <- Mid front left
            # top <- left, front <- front
        self.top_layer['front_middle'].sides['top'] = self.mid_layer['front_left'].sides['left']
        self.top_layer['front_middle'].sides['front'] = self.mid_layer['front_left'].sides['front']

        # Mid front left <- Bot front middle
            # left <- bottom, front <- front
        self.mid_layer['front_left'].sides['left'] = self.bot_layer['front_middle'].sides['bottom']
        self.mid_layer['front_left'].sides['front'] = self.bot_layer['front_middle'].sides['front']

        # Bot front middle <- Mid front right
            # bottom <- right, front <- front
        self.bot_layer['front_middle'].sides['bottom'] = self.mid_layer['front_right'].sides['right']
        self.bot_layer['front_middle'].sides['front'] = self.mid_layer['front_right'].sides['front']

        # Mid front right <- Top front middle
            # right <- top, front <- front
        self.mid_layer['front_right'].sides['right'] = edge_a
        self.mid_layer['front_right'].sides['front'] = edge_b
    
    def _F_prime(self):
        '''
        Turn front face counter-clockwise
        '''
        print("initiating _F_prime turn")

        # CORNERS #

        # Temp variables to protect against overwriting as we go
        corner_a = self.top_layer['front_left'].sides['left']
        corner_b = self.top_layer['front_left'].sides['top']
        corner_c = self.top_layer['front_left'].sides['front']

        # Top front left <- Top front right
            # left <- top, top <- right, front <- front 
        self.top_layer['front_left'].sides['left'] = self.top_layer['front_right'].sides['top']
        self.top_layer['front_left'].sides['top'] = self.top_layer['front_right'].sides['right']
        self.top_layer['front_left'].sides['front'] = self.top_layer['front_right'].sides['front']
        
        
        # Top front right <- Bot front right
            # top <- right, right <- bottom, front <- front
        self.top_layer['front_right'].sides['top'] = self.bot_layer['front_right'].sides['right']
        self.top_layer['front_right'].sides['right'] = self.bot_layer['front_right'].sides['bottom']
        self.top_layer['front_right'].sides['front'] = self.bot_layer['front_right'].sides['front']

        # Bot front right <- Bot front left
            # right <- bottom, bottom <- left, front <- front
        self.bot_layer['front_right'].sides['right'] = self.bot_layer['front_left'].sides['bottom']
        self.bot_layer['front_right'].sides['bottom'] = self.bot_layer['front_left'].sides['left']
        self.bot_layer['front_right'].sides['front'] = self.bot_layer['front_left'].sides['front']

        # Bot front left <- Top front left (temp)
            # bottom <- left, left <- top, front <- front
        self.bot_layer['front_left'].sides['bottom'] = corner_a
        self.bot_layer['front_left'].sides['left'] = corner_b
        self.bot_layer['front_left'].sides['front'] = corner_c

        # EDGES #

        # Temp variables to protect against overwriting as we go
        edge_a = self.top_layer['front_middle'].sides['top']
        edge_b = self.top_layer['front_middle'].sides['front']

        # Top front middle <- Mid front right
            # top <- right, front <- front
        self.top_layer['front_middle'].sides['top'] = self.mid_layer['front_right'].sides['right']
        self.top_layer['front_middle'].sides['front'] = self.mid_layer['front_right'].sides['front']

        # Mid front right <- Bot front middle
            # right <- bottom, front <- front
        self.mid_layer['front_right'].sides['right'] = self.bot_layer['front_middle'].sides['bottom']
        self.mid_layer['front_right'].sides['front'] = self.bot_layer['front_middle'].sides['front']

        # Bot front middle <- Mid front left
            # bottom <- left, front <- front
        self.bot_layer['front_middle'].sides['bottom'] = self.mid_layer['front_left'].sides['left']
        self.bot_layer['front_middle'].sides['front'] = self.mid_layer['front_left'].sides['front']

        # Mid front left <- Top front middle (temp)
            # left <- top, front <- front
        self.mid_layer['front_left'].sides['left'] = edge_a
        self.mid_layer['front_left'].sides['front'] = edge_b
    
    def _B(self):
        '''
        Turn back face clockwise
        '''
        print("initiating _B turn")

        # CORNERS #

        # Temp variable to protect against overwriting as we go
        corner_a = self.top_layer['back_right'].sides['top']
        corner_b = self.top_layer['back_right'].sides['right']
        corner_c = self.top_layer['back_right'].sides['back']

        # Top back right <- Bot back right
            # top <- right, right <- bottom, back <- back
        self.top_layer['back_right'].sides['top'] = self.bot_layer['back_right'].sides['right']
        self.top_layer['back_right'].sides['right'] = self.bot_layer['back_right'].sides['bottom']
        self.top_layer['back_right'].sides['back'] = self.bot_layer['back_right'].sides['back']


        # Bot back right <- Bot back left
            # right <- bottom, bottom <- left, back <- back
        self.bot_layer['back_right'].sides['right'] = self.bot_layer['back_left'].sides['bottom']
        self.bot_layer['back_right'].sides['bottom'] = self.bot_layer['back_left'].sides['left']
        self.bot_layer['back_right'].sides['back'] = self.bot_layer['back_left'].sides['back']

        # Bot back left <- Top back left
            # bottom <- left, left <- top, back <- back
        self.bot_layer['back_left'].sides['bottom'] = self.top_layer['back_left'].sides['left']
        self.bot_layer['back_left'].sides['left'] = self.top_layer['back_left'].sides['top']
        self.bot_layer['back_left'].sides['back'] = self.top_layer['back_left'].sides['back']

        # Top back left <- Top back right (temp)
            # left <- top, top <- right, back <- back
        self.top_layer['back_left'].sides['left'] = corner_a
        self.top_layer['back_left'].sides['top'] = corner_b
        self.top_layer['back_left'].sides['back'] = corner_c


        # EDGES #
        
        # Temp variable to protect against overwriting as we go
        edge_a = self.top_layer['back_middle'].sides['top']
        edge_b = self.top_layer['back_middle'].sides['back']

        # Top back middle <- Mid back right
            # top <- right, back <- back 
        self.top_layer['back_middle'].sides['top'] = self.mid_layer['back_right'].sides['right']
        self.top_layer['back_middle'].sides['back'] = self.mid_layer['back_right'].sides['back']

        # Mid back right <- Bot back middle
            # right <- bottom, back <- back
        self.mid_layer['back_right'].sides['right'] = self.bot_layer['back_middle'].sides['bottom']
        self.mid_layer['back_right'].sides['back'] = self.bot_layer['back_middle'].sides['back']

        # Bot back middle <- Mid back left
            # bottom <- left, back <- back
        self.bot_layer['back_middle'].sides['bottom'] = self.mid_layer['back_left'].sides['left']
        self.bot_layer['back_middle'].sides['back'] = self.mid_layer['back_left'].sides['back']


        # Mid back left <- Top back middle (temp)
            # left <- top, back <- back
        self.mid_layer['back_left'].sides['left'] = edge_a
        self.mid_layer['back_left'].sides['back'] = edge_b
    
    def _B_prime(self):
        '''
        Turn back face counter-clockwise
        '''
        print("initiating _B_prime turn")

        # CORNERS #

        # Temp variable to potect against overwriting as we go
        corner_a = self.top_layer['back_right'].sides['right']
        corner_b = self.top_layer['back_right'].sides['top']
        corner_c = self.top_layer['back_right'].sides['back']

        # Top back right <- Top back left
            # right <- top, top <- left, back <- back
        self.top_layer['back_right'].sides['right'] = self.top_layer['back_left'].sides['top']
        self.top_layer['back_right'].sides['top'] = self.top_layer['back_left'].sides['left']
        self.top_layer['back_right'].sides['back'] = self.top_layer['back_left'].sides['back']

        # Top back left <- Bot back left
            # top <- left, left <- bottom, back <- back
        self.top_layer['back_left'].sides['top'] = self.bot_layer['back_left'].sides['left']
        self.top_layer['back_left'].sides['left'] = self.bot_layer['back_left'].sides['bottom']
        self.top_layer['back_left'].sides['back'] = self.bot_layer['back_left'].sides['back']

        # Bot back left <- Bot Back right
            # left <- bottom, bottom <- right, back <- back
        self.bot_layer['back_left'].sides['left'] = self.bot_layer['back_right'].sides['bottom']
        self.bot_layer['back_left'].sides['bottom'] = self.bot_layer['back_right'].sides['right']
        self.bot_layer['back_left'].sides['back'] = self.bot_layer['back_right'].sides['back']

        # Bot back right <- Top back right (temp)
            # bottom <- right, right <- top, back <- back
        self.bot_layer['back_right'].sides['bottom'] = corner_a
        self.bot_layer['back_right'].sides['right'] = corner_b
        self.bot_layer['back_right'].sides['back'] = corner_c

        # EDGES #

        # Temp variable to store first overwritten sides
        edge_a = self.top_layer['back_middle'].sides['top']
        edge_b = self.top_layer['back_middle'].sides['back']

        # top back middle <- mid back left
            # top <- left, back <- back 
        self.top_layer['back_middle'].sides['top'] = self.mid_layer['back_left'].sides['left']
        self.top_layer['back_middle'].sides['back'] = self.mid_layer['back_left'].sides['back']

        # mid back left <- bot back middle
            # left <- bottom, back <- back
        self.mid_layer['back_left'].sides['left'] = self.bot_layer['back_middle'].sides['bottom']
        self.mid_layer['back_left'].sides['back'] = self.bot_layer['back_middle'].sides['back']

        # bot back middle <- mid back right
            # bottom <- right, back <- back
        self.bot_layer['back_middle'].sides['bottom'] = self.mid_layer['back_right'].sides['right']
        self.bot_layer['back_middle'].sides['back'] = self.mid_layer['back_right'].sides['back']

        # mid back right <- top back middle (temp)
            # right <- top, back <- back
        self.mid_layer['back_right'].sides['right'] = edge_a
        self.mid_layer['back_right'].sides['back'] = edge_b
        
    def _U(self):
        '''
        Turn upward face clockwise
        '''
        print("initiating _U turn")
        
        # CORNERS #

        # Temp variable to store first overwritten corner
        corner_a = self.top_layer['front_right'].sides['front']
        corner_b = self.top_layer['front_right'].sides['right']
        corner_c = self.top_layer['front_right'].sides['top']

        # Top front right <- Top back right
            # front <- right, right <- back, top <- top
        self.top_layer['front_right'].sides['front'] = self.top_layer['back_right'].sides['right']
        self.top_layer['front_right'].sides['right'] = self.top_layer['back_right'].sides['back']
        self.top_layer['front_right'].sides['top'] = self.top_layer['back_right'].sides['top']

        # Top back right <- Top back left
            # right <- back, back <- left, top <- top
        self.top_layer['back_right'].sides['right'] = self.top_layer['back_left'].sides['back']
        self.top_layer['back_right'].sides['back'] = self.top_layer['back_left'].sides['left']
        self.top_layer['back_right'].sides['top'] = self.top_layer['back_left'].sides['top']

        # Top back left <- Top front left
            # back <- left, left <- front, top <- top
        self.top_layer['back_left'].sides['back'] = self.top_layer['front_left'].sides['left']
        self.top_layer['back_left'].sides['left'] = self.top_layer['front_left'].sides['front']
        self.top_layer['back_left'].sides['top'] = self.top_layer['front_left'].sides['top']

        # Top front left <- Top front right (temp)
            # left <- front, front <- right, top <- top
        self.top_layer['front_left'].sides['left'] = corner_a
        self.top_layer['front_left'].sides['front'] = corner_b
        self.top_layer['front_left'].sides['top'] = corner_c

        # EDGES #

        # Temp variable to store first overwritten edge
        edge_a = self.top_layer['front_middle'].sides['front']
        edge_b = self.top_layer['front_middle'].sides['top']

        # Top front middle <- Top right middle
            # front <- right, top <- top
        self.top_layer['front_middle'].sides['front'] = self.top_layer['right_middle'].sides['right']
        self.top_layer['front_middle'].sides['top'] = self.top_layer['right_middle'].sides['top']

        # Top right middle <- Top back middle
            # right <- back, top <- top
        self.top_layer['right_middle'].sides['right'] = self.top_layer['back_middle'].sides['back']
        self.top_layer['right_middle'].sides['top'] = self.top_layer['back_middle'].sides['top']

        # Top back middle <- Top left middle
            # back <- left, top <- top
        self.top_layer['back_middle'].sides['back'] = self.top_layer['left_middle'].sides['left']
        self.top_layer['back_middle'].sides['top'] = self.top_layer['left_middle'].sides['top']

        # Top left middle <- Top front middle (temp)
            # left <- front, top <- top
        self.top_layer['left_middle'].sides['left'] = edge_a
        self.top_layer['left_middle'].sides['top'] = edge_b
        
    
    def _U_prime(self):
        '''
        Turn upward face counter-clockwise
        '''
        print("initiating _U_prime turn")

        # CORNERS #

        # temp variable to protect against overwrite
        corner_a = self.top_layer['front_right'].sides['right']
        corner_b = self.top_layer['front_right'].sides['front']
        corner_c = self.top_layer['front_right'].sides['top']

        # Top front right <- Top front left
            # right <- front, front <- left, top <- top
        self.top_layer['front_right'].sides['right'] = self.top_layer['front_left'].sides['front']
        self.top_layer['front_right'].sides['front'] = self.top_layer['front_left'].sides['left']
        self.top_layer['front_right'].sides['top'] = self.top_layer['front_left'].sides['top']

        # Top front left <- Top back left
            # front <- left, left <- back, top <- top
        self.top_layer['front_left'].sides['front'] = self.top_layer['back_left'].sides['left']
        self.top_layer['front_left'].sides['left'] = self.top_layer['back_left'].sides['back']
        self.top_layer['front_left'].sides['top'] = self.top_layer['back_left'].sides['top']

        # Top back left <- Top back right
            # left <- back, back <- right, top <- top
        self.top_layer['back_left'].sides['left'] = self.top_layer['back_right'].sides['back']
        self.top_layer['back_left'].sides['back'] = self.top_layer['back_right'].sides['right']
        self.top_layer['back_left'].sides['top'] = self.top_layer['back_right'].sides['top']

        # Top back right <- Top front right (temp)
            # back <- right, right <- front, top <- top
        self.top_layer['back_right'].sides['back'] = corner_a
        self.top_layer['back_right'].sides['right'] = corner_b
        self.top_layer['back_right'].sides['top'] = corner_c

        # EDGES #

        # temp variable to protect against overwrite
        edge_a = self.top_layer['front_middle'].sides['front']
        edge_b = self.top_layer['front_middle'].sides['top']

        # Top front middle <- Top left middle
            # front <- left, top <- top
        self.top_layer['front_middle'].sides['front'] = self.top_layer['left_middle'].sides['left']
        self.top_layer['front_middle'].sides['top'] = self.top_layer['left_middle'].sides['top']
        
        # Top left middle <- Top back middle
            # left <- back, top <- top
        self.top_layer['left_middle'].sides['left'] = self.top_layer['back_middle'].sides['back']
        self.top_layer['left_middle'].sides['top'] = self.top_layer['back_middle'].sides['top']

        # Top back middle <- Top right middle 
            # back <- right, top <- top
        self.top_layer['back_middle'].sides['back'] = self.top_layer['right_middle'].sides['right']
        self.top_layer['back_middle'].sides['top'] = self.top_layer['right_middle'].sides['top']

        # Top right middle <- Top front middle (temp)
            # right <- front, top <- top
        self.top_layer['right_middle'].sides['right'] = edge_a
        self.top_layer['right_middle'].sides['top'] = edge_b

    def _D(self):
        '''
        Turn downward face clockwise
        '''
        print("initiating _D turn")
        # CORNERS #

        # temp variables to protect against overwrite
        corner_a = self.bot_layer['front_right'].sides['right']
        corner_b = self.bot_layer['front_right'].sides['front']
        corner_c = self.bot_layer['front_right'].sides['bottom']

        # bot front right <- bot front left
            # right <- front, front <- left, bot <- bot
        self.bot_layer['front_right'].sides['right'] = self.bot_layer['front_left'].sides['front']
        self.bot_layer['front_right'].sides['front'] = self.bot_layer['front_left'].sides['left']
        self.bot_layer['front_right'].sides['bottom'] = self.bot_layer['front_left'].sides['bottom']

        # bot front left <- bot back left
            # front <- left, left <- back, bot <- bot
        self.bot_layer['front_left'].sides['front'] = self.bot_layer['back_left'].sides['left']
        self.bot_layer['front_left'].sides['left'] = self.bot_layer['back_left'].sides['back']
        self.bot_layer['front_left'].sides['bottom'] = self.bot_layer['back_left'].sides['bottom']

        # bot back left <- bot back right
            # left <- back, back <- right, bot <- bot
        self.bot_layer['back_left'].sides['left'] = self.bot_layer['back_right'].sides['back']
        self.bot_layer['back_left'].sides['back'] = self.bot_layer['back_right'].sides['right']
        self.bot_layer['back_left'].sides['bottom'] = self.bot_layer['back_right'].sides['bottom']

        # bot back right <- bot front right (temp)
            # back <- right, right <- front, bot <- bot
        self.bot_layer['back_right'].sides['back'] = corner_a
        self.bot_layer['back_right'].sides['right'] = corner_b
        self.bot_layer['back_right'].sides['bottom'] = corner_c

        # EDGES #

        # temp variable to protect against overwrite
        edge_a = self.bot_layer['front_middle'].sides['front']
        edge_b = self.bot_layer['front_middle'].sides['bottom']

        # bot front middle <- bot left middle
            # front <- left, bot <- bot
        self.bot_layer['front_middle'].sides['front'] = self.bot_layer['left_middle'].sides['left']
        self.bot_layer['front_middle'].sides['bottom'] = self.bot_layer['left_middle'].sides['bottom']

        # bot left middle <- bot back middle
            # left <- back, bot <- bot
        self.bot_layer['left_middle'].sides['left'] = self.bot_layer['back_middle'].sides['back']
        self.bot_layer['left_middle'].sides['bottom'] = self.bot_layer['back_middle'].sides['bottom']

        # bot back middle <- bot right middle
            # back <- right, bot <- bot
        self.bot_layer['back_middle'].sides['back'] = self.bot_layer['right_middle'].sides['right']
        self.bot_layer['back_middle'].sides['bottom'] = self.bot_layer['right_middle'].sides['bottom']

        # bot right middle <- bot front middle (temp)
            # right <- front, bot <- bot
        self.bot_layer['right_middle'].sides['right'] = edge_a
        self.bot_layer['right_middle'].sides['bottom'] = edge_b
    
    def _D_prime(self):
        '''
        Turn downward face counter-clockwise
        '''
        print("initiating _D_prime turn")
        # CORNERS #

        # temp variable to protect against overwrite
        corner_a = self.bot_layer['front_right'].sides['front']
        corner_b = self.bot_layer['front_right'].sides['right']
        corner_c = self.bot_layer['front_right'].sides['bottom']

        # bot front right <- bot back right
            # front <- right, right <- back, bottom <- bottom
        self.bot_layer['front_right'].sides['front'] = self.bot_layer['back_right'].sides['right']
        self.bot_layer['front_right'].sides['right'] = self.bot_layer['back_right'].sides['back']
        self.bot_layer['front_right'].sides['bottom'] = self.bot_layer['back_right'].sides['bottom']

        # bot back right <- bot back left
            # right <- back, back <- left, bottom <- bottom 
        self.bot_layer['back_right'].sides['right'] = self.bot_layer['back_left'].sides['back']
        self.bot_layer['back_right'].sides['back'] = self.bot_layer['back_left'].sides['left']
        self.bot_layer['back_right'].sides['bottom'] = self.bot_layer['back_left'].sides['bottom']

        # bot back left <- bot front left
            # back <- left, left <- front, bottom <- bottom
        self.bot_layer['back_left'].sides['back'] = self.bot_layer['front_left'].sides['left']
        self.bot_layer['back_left'].sides['left'] = self.bot_layer['front_left'].sides['front']
        self.bot_layer['back_left'].sides['bottom'] = self.bot_layer['front_left'].sides['bottom']

        # bot front left <- bot front right (temp)
            # left <- front, front <- right, bottom <- bottom
        self.bot_layer['front_left'].sides['left'] = corner_a
        self.bot_layer['front_left'].sides['front'] = corner_b
        self.bot_layer['front_left'].sides['bottom'] = corner_c

        # EDGES #

        # temp variable to protect against overwrite
        edge_a = self.bot_layer['front_middle'].sides['front']
        edge_b = self.bot_layer['front_middle'].sides['bottom']

        # bot front middle <- bot right middle
            # front <- right, bottom <- bottom
        self.bot_layer['front_middle'].sides['front'] = self.bot_layer['right_middle'].sides['right']
        self.bot_layer['front_middle'].sides['bottom'] = self.bot_layer['right_middle'].sides['bottom']
        
        # bot right middle <- bot back middle
            # right <- back, bottom <- bottom
        self.bot_layer['right_middle'].sides['right'] = self.bot_layer['back_middle'].sides['back']
        self.bot_layer['right_middle'].sides['bottom'] = self.bot_layer['back_middle'].sides['bottom']
        
        # bot back middle <- bot left middle
            # back <- left, bottom <- bottom
        self.bot_layer['back_middle'].sides['back'] = self.bot_layer['left_middle'].sides['left']
        self.bot_layer['back_middle'].sides['bottom'] = self.bot_layer['left_middle'].sides['bottom']

        # bot left middle <- bot front middle (temp)
            # left <- front, bottom <- bottom
        self.bot_layer['left_middle'].sides['left'] = edge_a
        self.bot_layer['left_middle'].sides['bottom'] = edge_b
    
    def _check_top_edges(self, match_color):

        faces = ['front', 'left', 'back', 'right']
        for face in faces:
            edge = self.top_layer[f'{face}_middle']
            if edge.sides[face] == match_color:
                return face
    
    def _handle_top_layer_edges(self, match_color):
        face = self._check_top_edges(match_color)
        while face is not None:
            if face == 'right':
                self._R_prime()
                self._U()
                self._F_prime()
            elif face == 'front':
                self._F_prime()
                self._U()
                self._L_prime()
            elif face == 'left':
                self._L_prime()
                self._U()
                self._B_prime()
            elif face == 'back':
                self._B_prime()
                self._U()
                self._R_prime()
            
            face = self._check_top_edges(match_color)
        
        self._handle_mid_layer_edges(match_color)

    def _check_mid_edges(self, match_color):
        # need to return both the face and the side
        # side tells us which face to turn, 
        # face tells us which way to turn

        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                edge = self.mid_layer[piece] 
                if edge.sides[v] == match_color:
                    return piece, v, h
                elif edge.sides[h] == match_color:
                    return piece, h, v
        return None, None, None
    
    def _handle_mid_layer_edges(self, match_color):
        piece, side, face = self._check_mid_edges(match_color)
        while piece is not None:

            # if we know the 2 'directions' separately
            # reference the side its on by that direction
            # reference the place is going by the other direction + middle
            # locate the correct direction by joining them (always need [front, back] first)
            # first-pass: return 3 values from func
            while self.top_layer[f'{face}_middle'].sides['top'] == match_color:
                self._U()

            if piece == 'front_right':
                if side == 'right':
                    self._F_prime()
                elif side == 'front':
                    self._R()

            elif piece == 'front_left':
                if side == 'left':
                    self._F()
                elif side == 'front':
                    self._L_prime()
            
            elif piece == 'back_right':
                if side == 'right':
                    self._B()
                elif side == 'back':
                    self._R_prime()
            
            elif piece == 'back_left':
                if side == 'left':
                    self._B_prime()
                elif side == 'back':
                    self._L()


            piece, side, face = self._check_mid_edges(match_color)

    
    def _check_bot_edges(self, match_color):

        faces = ['front', 'left', 'back', 'right']

        for face in faces:
            edge = self.bot_layer[f'{face}_middle']
            if edge.sides[face] == match_color:
                return face
    
    def _handle_bot_layer_edges(self, match_color):
        face = self._check_bot_edges(match_color)
        while face is not None:
            while self.top_layer[f'{face}_middle'].sides['top'] == match_color:
                self._U()
            
            if face == 'front':
                self._F()
                self._U()
                self._L_prime()
            elif face == 'left':
                self._L()
                self._U()
                self._B_prime()
            elif face == 'back':
                self._B()
                self._U()
                self._R_prime()
            elif face == 'right':
                self._R()
                self._U()
                self._F_prime()
        
            face = self._check_bot_edges(match_color)
        
        self._handle_mid_layer_edges(match_color)
        self._handle_top_layer_edges(match_color)

    
    def _check_bot_face(self, match_color):

        faces = ['front', 'left', 'back', 'right']

        for face in faces:
            edge = self.bot_layer[f'{face}_middle']
            if edge.sides['bottom'] == match_color:
                return face
    
    def _handle_bot_face_edges(self, match_color):
        face = self._check_bot_face(match_color)
        while face is not None:

            while self.top_layer[f'{face}_middle'].sides['top'] == match_color:
                self._U()
            
            if face == 'front':
                self._F()
                self._F()
            
            elif face == 'right':
                self._R()
                self._R()

            elif face == 'left':
                self._L()
                self._L()
            
            elif face == 'back':
                self._B()
                self._B()

            face = self._check_bot_face(match_color)

        self._handle_mid_layer_edges(match_color)
        self._handle_top_layer_edges(match_color)
        self._handle_bot_layer_edges(match_color)


    def _make_daisy(self):
        '''
        Bring 4 bottom color edge pieces to top layer, creating a daisy-like
        shape around that opposing center.
        '''
        # list the 4 edges, and solve them 1 at a time?
        # or keep looping the same logic until all 4 are done
        print("Making Daisy...")
        bottom_center = self.bot_layer['bottom_center'].sides['bottom']

        top_edges = [
            self.top_layer['front_middle'].sides,
            self.top_layer['left_middle'].sides,
            self.top_layer['right_middle'].sides,
            self.top_layer['back_middle'].sides,
        ]

        all_edges_white = all(edge['top'] == bottom_center for edge in top_edges)

        while not all_edges_white:

            # MID LAYER MATCHERS
            # if a middle edge matches, rotate top until the wrong color
            # is above it and turn it up
            self._handle_mid_layer_edges(bottom_center)

            # TOP LAYER MATCHERS
            # if the side face of a top edge matches, 
            # turn that face clockwise or counter,
            # turn the top the opposite way
            # turn the face it attached to the same opposite way

            # check top layer and return first instance of match or None
            self._handle_top_layer_edges(bottom_center)
                

            # BOT LAYER MATCHERS
            # if a bot layer edge matches,
            # rotate top until same face top edge isnt a match
            # rotate clockwise or counter
            # now treat like middle layer
            self._handle_bot_layer_edges(bottom_center)

            # The last remaining place for opposing edges is the bottom face
            # if the right color is on the bottom edge
            # we simply rotate the top until the corresponding side is is match free
            # the turn the piece up twice
            self._handle_bot_face_edges(bottom_center)
            all_edges_white = all(edge['top'] == bottom_center for edge in top_edges)

    def _check_bad_corners_bot_face(self, match_color):
        corners = [
            self.bot_layer['front_right'],
            self.bot_layer['front_left'],
            self.bot_layer['back_left'],
            self.bot_layer['back_right'],
        ]

        for corner in corners:
            if corner.sides['bottom'] == match_color:

                side_a, side_b = (side for side in corner.sides if side != 'bottom')
                if corner.sides[side_a] != self.mid_layer[f'{side_a}_center'].sides[side_a]:
                    return corner
                if corner.sides[side_b] != self.mid_layer[f'{side_b}_center'].sides[side_b]:
                    return corner
    
    def _handle_bad_corner(self, corner):

        if 'front' in corner.sides and 'right' in corner.sides:
            self._R()
            self._U()
            self._R_prime()
    
        elif 'front' in corner.sides and 'left' in corner.sides:
            self._L_prime()
            self._U()
            self._L()
        
        elif 'back' in corner.sides and 'left' in corner.sides:
            self._L()
            self._U()
            self._L_prime()

        elif 'back' in corner.sides and 'right' in corner.sides:
            self._R_prime()
            self._U()
            self._R()



    def _handle_problematic_crosses(self, match_color):
        # check bottom layer corners for white on the bottom face

        bad_corner = self._check_bad_corners_bot_face(match_color)

        while bad_corner is not None:

            self._handle_bad_corner(bad_corner)


            bad_corner = self._check_bad_corners_bot_face(match_color)

    def _bottom_cross(self):
        '''
        Move edge pieces from top to bottom, creating a cross shape in the 
        correct position on the bottom face.
        '''

        self._make_daisy()

        print("Making Bottom Cross...")

        bottom_center = self.bot_layer['bottom_center'].sides['bottom']


        # while any of the top edges match the bottom
        # while any(edge.sides['top'] == bottom_center for edge in top_edges):
        # find one that matches
        for face in ['front', 'left', 'back', 'right']:

            center = self.mid_layer[f'{face}_center'].sides[face]
            top = self.top_layer[f'{face}_middle'].sides['top']


            while (self.top_layer[f'{face}_middle'].sides[face], top) != (center, bottom_center):
                self._U()
                top = self.top_layer[f'{face}_middle'].sides['top']

            if face == 'front':
                self._F()
                self._F()
            elif face == 'right':
                self._R()
                self._R()
            elif face == 'back':
                self._B()
                self._B()
            elif face == 'left':
                self._L()
                self._L()
            # spin top until its other side matches the center
            # turn it down twice
    
    def _check_top_corners(self, match_color):

        # what do i need to return from this func
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                sides = [self.top_layer[piece].sides[side] for side in self.top_layer[piece].sides.keys() if side != 'top']
                if match_color in sides:
                    return self.top_layer[piece]
        
        return None
    
    def _handle_top_corners(self, piece, match_color):
        # move the whole while loop here
        # find the color on the side thats not the match or the top
        while piece is not None:
            other_color = self._get_other_color(piece, match_color)
            # find which center is that color
            face = self._find_matching_center(other_color)
            
            # turn until it matches
            # track same face color to match, and side colors to match bottom 
            if face in RubiksCube.horizontals:
                # face obvi needs to match
                # and then horizontal needs to match too 
                # good news is we know the piece we're matching
                while ((self.top_layer[f'front_{face}'].sides[face], self.top_layer[f'front_{face}'].sides['front']) != (other_color, match_color)
                and (self.top_layer[f'back_{face}'].sides[face], self.top_layer[f'back_{face}'].sides['back']) != (other_color, match_color)):
                    self._U()
                
                # now turn appropriately:
                side = self._get_side_color(face, match_color)
                self._bot_layer_trigger_helper(face, side)

            elif face in RubiksCube.verticals:
                while ((self.top_layer[f'{face}_right'].sides[face], self.top_layer[f'{face}_right'].sides['right']) != (other_color, match_color)
                and (self.top_layer[f'{face}_left'].sides[face], self.top_layer[f'{face}_left'].sides['left']) != (other_color, match_color)):
                    self._U()
            
                # get side
                side = self._get_side_color(face, match_color)
                self._bot_layer_trigger_helper(face, side)

            piece = self._check_top_corners(match_color)
        
        return
    
    def _find_matching_center(self, match_color):
            for face in ['front', 'right', 'back', 'left']:
                if self.mid_layer[f'{face}_center'].sides[face] == match_color:
                    return face
    
    def _get_other_color(self, piece, match_color):
        for side in piece.sides:
            if side != 'top' and piece.sides[side] != match_color:

                return piece.sides[side]
    
    def _get_side_color(self, face, match_color):
        if face in ['front', 'back']:
            face_side = self.top_layer[f'{face}_right'].sides[face]
            other_side = 'right'

            if ((face_side, self.top_layer[f'{face}_{other_side}'].sides[other_side]) == (self.mid_layer[f'{face}_center'].sides[face], match_color)):
                return other_side
            else:
                return 'left'

            
        elif face in ['left', 'right']:
            face_side = self.top_layer[f'front_{face}'].sides[face]
            other_side = 'front'

            if (face_side, self.top_layer[f'{other_side}_{face}'].sides[other_side]) == (self.mid_layer[f'{face}_center'].sides[face], match_color):
                return other_side
            else:
                return 'back'

        
    
    def _bot_layer_trigger_helper(self, face, side):

        # first we note face
        if face == 'front':
            # is it left or right?
            if side == 'left':
                self._L_prime()
                self._U_prime()
                self._L()
            elif side == 'right':
                self._R()
                self._U()
                self._R_prime()
        elif face == 'back':
            # left or right
            if side == 'right':
                self._R_prime()
                self._U_prime()
                self._R()
            elif side == 'left':
                self._L()
                self._U()
                self._L_prime()
        elif face == 'left':
            # front or back
            if side == 'front':
                self._F()
                self._U()
                self._F_prime()
            elif side == 'back':
                self._B_prime()
                self._U_prime()
                self._B()
        elif face == 'right':
            # front or back
            if side == 'front':
                self._F_prime()
                self._U_prime()
                self._F()
            elif side == 'back':
                self._B()
                self._U()
                self._B_prime()

    def _check_top_face(self, match_color):
        for top in self.top_layer:
            if self.top_layer[top].sides['top'] == match_color:
                return top
        
        return None
    
    def _find_mismatched_bottom(self, match_color):
            for bottom in self.bot_layer:
                if self.bot_layer[bottom].sides['bottom'] != match_color:
                        return bottom
    
    def _get_next_location(self, pieces, previous_location):
        if pieces == 'corners':
            if previous_location == 'front_right':
                location = 'front_left'
            elif previous_location == 'front_left':
                location = 'back_left'
            elif previous_location == 'back_left':
                location = 'back_right'
            elif previous_location == 'back_right':
                location = 'front_right'
        
        elif pieces == 'edges':
            if previous_location == 'front':
                location = 'left'
            elif previous_location == 'left':
               location = 'back'
            elif previous_location == 'back':
                location = 'right'
            elif previous_location == 'right':
                location = 'front'
    
        return location


    def _handle_top_face(self, top_location, match_color):

        while top_location is not None:

            # find the piece with bottom thats the wrong color
            bottom_location = self._find_mismatched_bottom(match_color)


            # rotate top until the right color is the same piece 
            while top_location != bottom_location:
                self._U()
                top_location = self._get_next_location('corners', top_location)
            # double trigger -> front and back should cover all bases
            v, h = top_location.split('_')
            self._bot_layer_double_trigger_helper(v, h)
            
            piece = self._check_top_corners(match_color)
            self._handle_top_corners(piece, match_color)
            
            # handle top corners 
            top_location = self._check_top_face(match_color)
        
        return
 
    def _bot_layer_double_trigger_helper(self, v, h):

        # if front
        if v == 'front':
            # if right
            if h == 'right':
                # R, U, U, R`
                self._R()
                self._U()
                self._U()
                self._R_prime()
            # if left
            elif h == 'left':
                # L`, U, U, L
                self._L_prime()
                self._U()
                self._U()
                self._L()
        # if back
        elif v == 'back':
            # if right
            if h == 'right':
                # R`, U, U, R
                self._R_prime()
                self._U()
                self._U()
                self._R()
            # if left
            elif h == 'left':
                # L, U, U, L`
                self._L()
                self._U()
                self._U()
                self._L_prime()
    
    def _check_bot_corners(self, match_color):
        # THis is ugly. make better.
    
        for corner in self.bot_layer:
            if 'middle' not in corner and 'center' not in corner:
                for side in self.bot_layer[corner].sides:
                    if self.bot_layer[corner].sides[side] == match_color and side != 'bottom':
                        return corner

        return None

    def _handle_bottom_corners(self, bottom_location, match_color):

        while bottom_location is not None:
            v, h = bottom_location.split("_")

            self._bot_layer_trigger_helper(v, h)
            top_location = self._check_top_face(match_color)
            self._handle_top_face(top_location, match_color)

            bottom_location = self._check_bot_corners(match_color)

    def _solve_bot_layer(self):
        '''
        Solve the rest of the bottom layer, and in the process, the bottom
        face.
        '''

        self._bottom_cross()

        print("Solving bottom layer...")

        bottom_center = self.bot_layer['bottom_center'].sides['bottom']

        self._handle_problematic_crosses(bottom_center)

        # ALL CODE UNDER THIS NEEDS TO RUN INSIDE WHILE BOTTOM FACE NOT ALL THE SAME
        while not all(self.bot_layer[bottom].sides['bottom'] == bottom_center for bottom in self.bot_layer):

            # find a piece that has match_color on it (not on top side)
            piece = self._check_top_corners(bottom_center)
            self._handle_top_corners(piece, bottom_center)

            # when out of not top side pieces, look for top side
            top_location = self._check_top_face(bottom_center)
            self._handle_top_face(top_location, bottom_center)
                
            # when out of all top row matches, must be on the bottom
            bottom_location = self._check_bot_corners(bottom_center)
            self._handle_bottom_corners(bottom_location, bottom_center)
        
    
    def _mid_layer_solved(self):
        edges = [
            self.mid_layer['front_right'],
            self.mid_layer['front_left'],
            self.mid_layer['back_left'],
            self.mid_layer['back_right'],
        ]

        for edge in edges:
            for side in edge.sides:
                if edge.sides[side] != self.mid_layer[f'{side}_center'].sides[side]:
                    return False
        
        return True

    def _non_yellow_top(self):
        for face in ['front', 'left', 'back', 'right']:
            edge = self.top_layer[f'{face}_middle']
            if 'y' not in edge.sides.values():
                return face
    
    def _handle_mid_layer_get_opposing_face(self, match_color):
        for color_pair in self.opposing_colors:
            color_a, color_b = color_pair

            if color_a == match_color:
                for face in ['front', 'left', 'back', 'right']:
                    if self.mid_layer[f'{face}_center'].sides[face] == color_b:
                        return face

            if color_b == match_color:
                for face in ['front', 'left', 'back', 'right']:
                    if self.mid_layer[f'{face}_center'].sides[face] == color_a:
                        return face

    def _handle_mid_layer_align_opposing_colors(self, matching_face, opposing_face):
        # turn the piece - what does that mean
        while matching_face != opposing_face:
            self._U()
            matching_face = self._get_next_location('edges', matching_face)
    
    def _handle_mid_layer_trigger_helper(self, top_color, side_color):
        # first get the face which matches the top color
        top_color_face = self._find_matching_center(top_color)
        # then the face that matches the side color
        side_color_face = self._find_matching_center(side_color)
        
        # pass to trigger helper with side as main and top as secondary
        self._bot_layer_trigger_helper(side_color_face, top_color_face)

        piece = self._check_top_corners('w')
        self._handle_top_corners(piece, 'w')

    def _handle_mid_layer_top_piece(self, matching_face):
        # get the top side color
        top_color = self.top_layer[f'{matching_face}_middle'].sides['top']
        side_color = self.top_layer[f'{matching_face}_middle'].sides[matching_face]
        # find its opposite
        oppo_face = self._handle_mid_layer_get_opposing_face(top_color)
        
        # turn til aligned
        self._handle_mid_layer_align_opposing_colors(matching_face, oppo_face)
        # figure out which way non-top side is
        self._handle_mid_layer_trigger_helper(top_color, side_color)
        # handle appropriate turns
    
    def _get_mismatched_middle_edge(self):
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                for side in self.mid_layer[piece].sides:
                    if self.mid_layer[piece].sides[side] != self.mid_layer[f'{side}_center'].sides[side]:
                        return piece

    def _handle_mid_layer_middle_piece(self):
        # find middle edges that are out of place
        mismatched_piece = self._get_mismatched_middle_edge()
        face, side = mismatched_piece.split("_")
        self._bot_layer_trigger_helper(face, side)

        white_piece = self._check_top_corners('w')
        self._handle_top_corners(white_piece, 'w')

        # matching_face = self._non_yellow_top()
        # self._handle_mid_layer_top_piece(matching_face)


        # trigger them up to the top
        # top trigger we once again will need to know 2 faces in some order
        pass

    def _solve_mid_layer(self):
        '''
        Solve the middle layer of the cube
        '''

        self._solve_bot_layer()

        print("Solving Middle Layer...")

        layer_complete = self._mid_layer_solved()

        while not layer_complete:
            # first check the top layer for edges that dont have yellow
            matching_face = self._non_yellow_top()
            # those edges get aligned properly 
            if matching_face is not None:
                self._handle_mid_layer_top_piece(matching_face)
        
            elif not matching_face:
                self._handle_mid_layer_middle_piece()
        # second it must mispositioned in the middle layer somewhere
            # first trigger it out onto the top
            # then back to the first part
            layer_complete = self._mid_layer_solved()
    
    def _top_cross_solved(self):
        for face in ['front', 'left', 'back', 'right']:
            if self.top_layer[f'{face}_middle'].sides['top'] != 'y':
                return False
        
        return True
    
    def _get_yellow_edges(self):
        yellow_edges = []
        for face in ['front', 'left', 'back', 'right']:
            if self.top_layer[f'{face}_middle'].sides['top'] == 'y':
                yellow_edges.append(face)
        
        return yellow_edges
    
    def _FURURF(self):
        self._F()
        self._U()
        self._R()
        self._U_prime()
        self._R_prime()
        self._F_prime()
    
    def _get_nine_twelve_colors(self):
        return [
            self.top_layer['left_middle'].sides['top'],
            self.top_layer['back_middle'].sides['top']
        ]
    
    def _handle_top_cross_turns(self, yellow_edges):

        # if no edges are yellow, just F U R U` R` F`
        if len(yellow_edges) == 0:
            self._FURURF()
        
        # if 2 edges are yellow
        elif len(yellow_edges) == 2:
            # if they are opposite each other, either F U R U` R` F` or R U B U` B` R`
            if set(yellow_edges) == set(RubiksCube.verticals):
                self._FURURF()
            elif set(yellow_edges) == set(RubiksCube.horizontals):
                self._R()
                self._U()
                self._B()
                self._U_prime()
                self._B_prime()
                self._R_prime()

            # if they are adjacent, rotate until its the left and the back
            else:
                nine_twelve = self._get_nine_twelve_colors()

                while not all(color == 'y' for color in nine_twelve):
                    self._U()
                    nine_twelve = self._get_nine_twelve_colors()
                
                self._FURURF()

            
    def _solve_top_cross(self):
        '''
        Solve the cross on the top layer without messing up solved layers.
        '''

        self._solve_mid_layer()

        print("Solving Top Cross...")
        # so long as not all 4 edges are yellow
        edges_complete = self._top_cross_solved()

        while not edges_complete:
            yellow_edges = self._get_yellow_edges()
            self._handle_top_cross_turns(yellow_edges)

            edges_complete = self._top_cross_solved()
        
    def _count_yellow_corners(self):
        yellow_corners = 0
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                if self.top_layer[piece].sides['top'] == 'y':
                    yellow_corners += 1
        
        return yellow_corners
    
    def _RUR_prime(self):
        self._R()
        self._U()
        self._R_prime()
        self._U()
        self._R()
        self._U()
        self._U()
        self._R_prime()
    
    def _top_face_solved(self):
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                if self.top_layer[piece].sides['top'] != 'y':
                    return False
        
        return True
    
    def _solve_top_face(self):
        '''
        Complete the rest of the top face.
        '''
        self._solve_top_cross()

        print("Solving Top Face...")
        
        top_face_solved = self._top_face_solved()
        while not top_face_solved:


            # find how many corners we have
            yellow_corners = self._count_yellow_corners()

            # if none, rotate until the front left left-side is yellow
            if yellow_corners == 0:
                front_left = self.top_layer['front_left'].sides['left']
                while front_left != 'y':
                    self._U()
                    front_left = self.top_layer['front_left'].sides['left']
                # R U R` U R U U R`
                self._RUR_prime()

            # if one, rotate until its the front left top-side
            elif yellow_corners == 1:
                front_left = self.top_layer['front_left'].sides['top']
                while front_left != 'y':
                    self._U()
                    front_left = self.top_layer['front_left'].sides['top']
                # R U R` U R U U R`
                self._RUR_prime()

            # if two, rotate until the front left front-side is yellow,
            elif yellow_corners == 2:
                front_left = self.top_layer['front_left'].sides['front']
                while front_left != 'y':
                    self._U()
                    front_left = self.top_layer['front_left'].sides['front']
                # R U R` U R U U R`
                self._RUR_prime()

            top_face_solved = self._top_face_solved()
        
    def _get_matching_top_corners(self):
        faces = ['front', 'left', 'back', 'right']
        faces_dict = {face: [] for face in faces}
        for face in faces:
            for piece in ['front_right', 'front_left', 'back_left', 'back_right']:
                if face in self.top_layer[piece].sides:
                    faces_dict[face].append(self.top_layer[piece].sides[face])
        
        for face in faces_dict:
            if faces_dict[face][0] == faces_dict[face][1]:
                return faces_dict[face][0]
        
    def _check_all_four_corners(self):
        faces = ['front', 'left', 'back', 'right']
        faces_dict = {face: set() for face in faces}

        for piece in ['front_right', 'front_left', 'back_left', 'back_right']:
            for side in self.top_layer[piece].sides:
                if side != 'top':
                    faces_dict[side].add(self.top_layer[piece].sides[side])

        print(faces_dict)
        for face in faces_dict:
            if len(faces_dict[face]) != 1:
                return False
        
        return True

    
    def _LURULR(self):
        self._L_prime()
        self._U()
        self._R()
        self._U_prime()
        self._L()
        self._U()
        self._R_prime()
        self._RUR_prime()
    
    # def _check_solved_face(self):
        # faces = ['front', 'left', 'back', 'right']
        # faces_dict = {face: set() for face in faces}

        # for piece in ['front_right', 'front_left', 'back_left', 'back_right']:
        #     for side in self.top_layer[piece].sides:
        #         if side != 'top':
        #             faces_dict[side].add(self.top_layer[piece].sides[side])
        
        # for face in faces:
        #     for side in self.top_layer[f'{face}_middle'].sides:
        #         if side != 'top':
        #             faces_dict[face].add(self.top_layer[f'{face}_middle'].sides[side])

        # for face in faces_dict:
        #     if len(faces_dict[face]) == 1:
        #         return True
        
        # return False
    
    def _align_corners_to_face(self, matching_center):
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = f'{v}_{h}'
                if matching_center in self.top_layer[piece].sides:
                    corner_color = self.top_layer[piece].sides[matching_center]
                    while corner_color != self.mid_layer[f'{matching_center}_center'].sides[matching_center]:
                        self._U()
                        corner_color = self.top_layer[piece].sides[matching_center]

    def _handle_matching_corners_turns(self, matching_center):

        print("matching center:", matching_center)
        # if on the left, LUR func
        if matching_center == 'left':
            self._LURULR()
        
        # if on the back B` U F U` B U U F` U F U U F`
        elif matching_center == 'back':
            self._B_prime()
            self._U()
            self._F()
            self._U_prime()
            self._B()
            self._U()
            self._U()
            self._F_prime()
            self._U()
            self._F()
            self._U()
            self._U()
            self._F_prime()

        # if it's on the right R` U L U` R U U L` U L U U L`
        elif matching_center == 'right':
            self._R_prime()
            self._U()
            self._L()
            self._U_prime()
            self._R()
            self._U()
            self._U()
            self._L_prime()
            self._U()
            self._L()
            self._U()
            self._U()
            self._L_prime()

        # if it's on the front F` U B U` F U U B` U B U U B`
        elif matching_center == 'front':
            self._F_prime()
            self._U()
            self._B()
            self._U_prime()
            self._F()
            self._U()
            self._U()
            self._B_prime()
            self._U()
            self._B()
            self._U()
            self._U()
            self._B_prime()
            
    def _align_solved_corners(self):
        front_corners = [
            self.top_layer['front_right'],
            self.top_layer['front_left']
        ]

        corners_aligned = all(corner.sides['front'] == 'r' for corner in front_corners)
        while not corners_aligned:
            print([corner.sides['front'] for corner in front_corners])
            self._U()
            corners_aligned = all(corner.sides['front'] == 'r' for corner in front_corners)
        
    def _solve_top_corners(self):
        '''
        Solves top corners by getting them all to match each other
        '''
        self._solve_top_face()

        print("Solving Top Corners...")

        # need to do this so long as no one face is solved
        # solved_face = self._check_solved_face()
        all_four_corners = self._check_all_four_corners()

        while not all_four_corners:

            # print("Is there a solved face?", solved_face)
            print("Do all four corners match?", all_four_corners)
            # substitute that with no 3 top colors match each other (or maybe match their center but that seems silly)
            # find corners that match each other
            matching_corner = self._get_matching_top_corners()

            # if there are none, L` U R U` L U U R` U R U U R`
            if not matching_corner:
                self._LURULR()
            # if there is one, align it to its' face
            else:
                # find the center that matches
                matching_center = self._find_matching_center(matching_corner)

                # rotate until its aligned with the one it matches
                self._align_corners_to_face(matching_center)
                # figure out the turns needed
                self._handle_matching_corners_turns(matching_center)
            # handle those turns based on which face that is
            # solved_face = self._check_solved_face()
            # breakpoint()
            all_four_corners = self._check_all_four_corners()
        
        # align corners
        self._align_solved_corners()
    
    def _check_cube_solved(self):

        for face in ['front', 'left', 'back', 'right']:
            if self.top_layer[f'{face}_middle'].sides[face] != self.mid_layer[f'{face}_center'].sides[face]:
                return False
        
        for v in RubiksCube.verticals:
            for h in RubiksCube.horizontals:
                piece = self.top_layer[f'{v}_{h}']
                for side in piece.sides:
                    if side != 'top' and piece.sides[side] != self.mid_layer[f'{side}_center'].sides[side]:
                        return False
        
        return True
    
    def _get_solved_face(self):
        faces = ['front', 'left', 'back', 'right']
        faces_dict = {face: 0 for face in faces}
        
        for piece in self.top_layer:
            for side in self.top_layer[piece].sides:
                if side in faces_dict:
                    if self.top_layer[piece].sides[side] == self.mid_layer[f'{side}_center'].sides[side]:
                        faces_dict[side] += 1

        for face in faces_dict:
            if faces_dict[face] == 3:
                return face
    
    def _F_two_clockwise(self, solved_face=None):
        # solved face is right
        if solved_face == 'right':
            self._L()
            self._L()
            self._U()
            self._D()
            self._F_prime()
            self._L()
            self._L()
            self._D_prime()
            self._F()
            self._U()
            self._L()
            self._L()
        # solved face is front
        elif solved_face == 'front':
            self._B()
            self._B()
            self._U()
            self._R()
            self._L_prime()
            self._B()
            self._B()
            self._R_prime
            self._L()
            self._U()
            self._B()
            self._B()

        # solved face is left
        elif solved_face == 'left':
            self._R()
            self._R()
            self._U()
            self._F()
            self._B_prime()
            self._R()
            self._R()
            self._F_prime()
            self._B()
            self._U()
            self._R()
            self._R()

        # else (solved face is back or None)
        else:
            self._F()
            self._F()
            self._U()
            self._L()
            self._R_prime()
            self._F()
            self._F()
            self._L_prime()
            self._R()
            self._U()
            self._F()
            self._F()
    
    def solve_cube(self):
        '''
        User facing function to solve cube.
        '''
        self._solve_top_corners()

        print("Solving final step...")

        # as long as not all four top middles match their center
        solved = self._check_cube_solved()
        while not solved:

            solved_face = self._get_solved_face()
            print("Solved Face", solved_face)

            # or just F F U L R` F F L` R U F F
            self._F_two_clockwise(solved_face)
            breakpoint()
            
            solved = self._check_cube_solved()


if __name__ == "__main__":
    cube = RubiksCube()
    cube.solve_cube()
