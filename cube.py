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
            or (color_pairs_count[(first_choice, second_choice)] + 
                color_pairs_count[(second_choice)] == 2)):
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
            or (color_pairs_count[(second_choice, third_choice)] +
            color_pairs_count[(third_choice, second_choice)] == 2)
            or ({first_choice, second_choice, third_choice}) in complete_corners):
                third_choice = random.choice(colors)
                
            # assign it
            corner.sides[side3] = third_choice

            # add corner to completed corners
            complete_corners.append({first_choice, second_choice, third_choice})
          
            print("Third choice in loop - ", third_choice)
            print("Color count", colors_count)
            print("color_pairs_count", color_pairs_count)


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

        print("Front left", self.top_layer['front_left'].sides)
        # Top back left <- Top front left
            # back <- top, top <- front, left <- left
        self.top_layer['back_left'].sides['back'] = self.top_layer['front_left'].sides['top']
        self.top_layer['back_left'].sides['top'] = self.top_layer['front_left'].sides['front']
        self.top_layer['back_left'].sides['left'] = self.top_layer['front_left'].sides['left']

        print("Back left", self.top_layer['back_left'].sides)
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

# << Tested until here >>
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
        self.bot_layer['left_middle'].sides['botom'] = edge_b

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

