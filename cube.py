'''
Class instantiation of a Rubik's Cube, with the logic to solve it.
'''

import random
from piece import Piece, Center, Edge, Corner

class RubiksCube:

    colors = ['w', 'y', 'o', 'b', 'r', 'g']
    
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
        
        self.opposing_colors = []
    
    def __repr__(self):
        return f"""RubiksCube({self.top_layer}, {self.mid_layer}, {self.bot_layer})"""

    def __str__(self):
        output = f"""
        Top layer: {self.top_layer}\n\n\n
        Middle layer: {self.mid_layer}\n\n\n
        Bottom layer: {self.bot_layer}\n\n\n"""
        return output
    
    def count_colors(self):
        '''
        After initializing the cube, use this to confirm each of the
        colors was placed 9 times.
        '''

        colors = {color: 0 for color in RubiksCube.colors}
        layers = [self.bot_layer, self.mid_layer, self.top_layer]
        for layer in layers:
            # Now we have a dict of pieces
            # For each key in the dict...
            for key in layer:
                # unpack the sides
                for side in layer[key].sides:
                # increment the value in the dict
                    colors[layer[key].sides[side]] += 1
        
        print(colors)

            

    def _initialize_centers(self):
        '''
        Initializes centers of cube by assigning each center a random color
        and removing that color from the choices after assignment.
        
        Also fills in the opposing_colors attribute list with tuples of each opposing pair.
        '''

        # List of colors
        colors = RubiksCube.colors.copy()

        # looping through center pieces
        for piece in self.centers:
            color = random.choice(colors)
            # assign it a random choice from the colors
            side = list(piece.sides.keys())[0]
            piece.sides[side] = color
            # remove that color from list
            colors.remove(color)

        self.opposing_colors.append(
            (self.bot_layer['bottom_center'].sides['bottom'], self.top_layer['top_center'].sides['top'])
            )
        self.opposing_colors.append(
            (self.top_layer['top_center'].sides['top'], self.bot_layer['bottom_center'].sides['bottom'])
            )
        self.opposing_colors.append(
            (self.mid_layer['right_center'].sides['right'], self.mid_layer['left_center'].sides['left'])
            )
        self.opposing_colors.append(
            (self.mid_layer['left_center'].sides['left'], self.mid_layer['right_center'].sides['right'])
            )
        self.opposing_colors.append(
            (self.mid_layer['front_center'].sides['front'], self.mid_layer['back_center'].sides['back'])
            )
        self.opposing_colors.append(
            (self.mid_layer['back_center'].sides['back'], self.mid_layer['front_center'].sides['front'])
            )

    def _initialize_edges(self):
        '''
        Initializes edge pieces of cube by assigning a random color to one side
        of the edge and picking another random color for the other side within
        constraints of cube layout - no opposing colors on the same piece, no 2
        pieces with the same 2 colors, and each color appearing on 4 total edge
        pieces.
        '''

        # list of colors again
        colors = RubiksCube.colors.copy()
        # dict to keep track of how many times each color has been used
        colors_count = {color: 0 for color in colors}
        # list of edges

        complete_edges = []
        # looping through edges
        for edge in self.edges:
            # get faces from dict to access
            side1, side2 = tuple(edge.sides.keys())

            # random choice from colors list
            first_choice = random.choice(colors) 
            # assign to side1
            edge.sides[side1] = first_choice

            # select another choice
            second_choice = random.choice(colors)
            # confirm its not the same or the opposing color
            while ((second_choice == first_choice)
            or ((first_choice, second_choice) in self.opposing_colors)
            or ({first_choice, second_choice} in complete_edges)):
                second_choice = random.choice(colors)

            # assign to second
            edge.sides[side2] = second_choice
            # append pair to list
            complete_edges.append({first_choice, second_choice})

            # increment both colors dict value
            colors_count[first_choice] += 1
            colors_count[second_choice] += 1
            if colors_count[first_choice] == 4:
                colors.remove(first_choice)
            if colors_count[second_choice] == 4:
                colors.remove(second_choice)

    def _initialize_corners(self):
        '''
        Initializes corner pieces of cube by assigning a random color to one side
        of the edge and picking 2 more random colors for the other 2 sides within
        constraints of cube layout - no opposing colors on the same piece, no 2
        pieces with the same 3 colors, and each color appears 4 times on corner
        pieces, with each color pair appearing twice.
        '''
        colors = RubiksCube.colors.copy()
        colors_count = {color: 0 for color in colors}

        color_pairs = []
        for color1 in colors:
            for color2 in colors:
                if color1 != color2 and (color1, color2) not in self.opposing_colors:
                    color_pairs.append((color1, color2))
        color_pairs_count = {color_pair: 0 for color_pair in color_pairs}
        
        complete_corners = []

        for corner in self.corners:
            # Tuple unpack the faces/sides
            side1, side2, side3 = tuple(corner.sides.keys())

            # choose random color
            first_choice = random.choice(colors)
            # assign to first side
            corner.sides[side1] = first_choice

            # choose second color
            second_choice = random.choice(colors)
            # if its the same as first or opposite side
            # keep choosing til its not
            while ((second_choice == first_choice)
            or ((first_choice, second_choice) in self.opposing_colors)
            or (color_pairs_count[(first_choice, second_choice)]
            + color_pairs_count[(second_choice, first_choice)] == 2)):
                second_choice = random.choice(colors)
            # assign to second side
            corner.sides[side2] = second_choice

            # choose third color from 2 colors adjacent to second color
            # Logic: once we've chosen 2 colors, the third color can onlybe one of two
            # Pick one of those - make sure not to repick by A adding piece to complete
            # B increment count of colors, C check second_choice that we're not picking
            # a two-color combo that's been picked twice already
            third_choice = random.choice(colors)
            while ((third_choice == first_choice) or (third_choice == second_choice)
            or ((first_choice, third_choice) in self.opposing_colors)
            or ((second_choice, third_choice) in self.opposing_colors)
            or (color_pairs_count[(first_choice, third_choice)] +
            color_pairs_count[(third_choice, first_choice)] == 2)
            or ({first_choice, second_choice, third_choice}) in complete_corners):
                #print("Third choice in loop - ", third_choice)
                third_choice = random.choice(colors)
                
            # assign it
            corner.sides[side3] = third_choice

            # increment each colors count
            colors_count[first_choice] += 1
            colors_count[second_choice] += 1
            colors_count[third_choice] += 1

            color_pairs_count[(first_choice, second_choice)] += 1 
            color_pairs_count[(first_choice, third_choice)] += 1 
            color_pairs_count[(third_choice, second_choice)] += 1 

            # if any are at 4 remove from list
            if colors_count[first_choice] == 4:
                colors.remove(first_choice)
            if colors_count[second_choice] == 4:
                colors.remove(second_choice)
            if colors_count[third_choice] == 4:
                colors.remove(third_choice)


    def initialize_cube(self):
        '''
        Function to call to initialize cube. Calls on helper functions for 
        centers, edges, and corners; in that order.
        '''

        self._initialize_centers()

        self._initialize_edges()

        self._initialize_corners()
    
    def _L(self):
        '''
        Turn left face clockwise
        '''

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

        # Bot left middle <- Mid back left
            # bottom <- back, left <- left
        self.bot_layer['left_middle'].sides['bottom'] = edge_a
        self.bot_layer['left_middle'].sides['left'] = edge_b

    def _L_prime(self):
        '''
        Turn left face counter-clockwise
        '''

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

        # CORNERS # 

        # Temp variables to protect against overwriting
        corner_a = self.top_layer['back_right'].sides['top']
        corner_b = self.top_layer['back_right'].sides['back']
        corner_a = self.top_layer['back_right'].sides['right']

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
        self.bot_layer['back_right'].sides['back'] = self.top_layer['back_right'].sides['top']
        self.bot_layer['back_right'].sides['bottom'] = self.top_layer['back_right'].sides['back']
        self.bot_layer['back_right'].sides['right'] = self.top_layer['back_right'].sides['right']
        
        # EDGES #

        # Temp variables to protect against overwrite

        # Top right middle <- Mid front right
            # top <- front, right <- right

        # Mid front right <- Bot right middle
            # front <- bottom, right <- right

        # Bot right middle <- Mid back right
            # bottom <- back, right <- right

        # Mid back right <- Top right middle (temp)
            # back <- top, right <- right            
    
    def _R_prime(self):
        '''
        Turn right face counter-clockwise
        '''

    def _F(self):
        '''
        Turn front face clockwise
        '''
        pass
    
    def _F_prime(self):
        '''
        Turn front face counter-clockwise
        '''
    
    def _B(self):
        '''
        Turn back face clockwise
        '''
        pass
    
    def _B_prime(self):
        '''
        Turn back face counter-clockwise
        '''
        
    def _U(self):
        '''
        Turn upward face clockwise
        '''
        pass
    
    def _U_prime(self):
        '''
        Turn upward face counter-clockwise
        '''

    def _D(self):
        '''
        Turn downward face clockwise
        '''
        pass
    
    def _D_prime(self):
        '''
        Turn downward face counter-clockwise
        '''

    def _make_daisy(self):
        '''
        Bring 4 bottom color edge pieces to top layer, creating a daisy-like
        shape around that opposing center.
        '''
        pass
    
    def _white_cross(self):
        '''
        Move edge pieces from top to bottom, creating a cross shape in the 
        correct position on the bottom face.
        '''
        pass
    
    def _solve_bot_layer(self):
        '''
        Solve the rest of the bottom layer, and in the process, the bottom
        face.
        '''
        pass
    
    def _solve_mid_layer(self):
        '''
        Solve the middle layer of the cube
        '''
        pass
    
    def _get_top_cross(self):
        '''
        Solve the cross on the top layer without messing up solved layers.
        '''
        pass
    
    def _solve_top_face(self):
        '''
        Complete the rest of the top face.
        '''
        pass
    
    def _final_step(self):
        '''
        Final solve step (this might actually need to be broken up into more
        steps).
        '''
        pass
    
    def solve_cube(self):
        '''
        User facing function to solve cube.
        '''

        self._make_daisy()

        self._white_cross()

        self._solve_bot_layer()

        self._solve_mid_layer()

        self._get_top_cross()

        self._solve_top_face()

        self._final_step()

