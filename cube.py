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

        -- This should be moved to a test --
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
                color_pairs_count[(second_choice, first_choice)] == 2)):
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
    
    def _check_mid_edges(self, match_color):
        # need to return both the face and the side
        # side tells us which face to turn, 
        # face tells us which way to turn
        verticals = ['front', 'back']
        horizontals = ['left', 'right']

        for v in verticals:
            for h in horizontals:
                piece = f'{v}_{h}'
                edge = self.mid_layer[piece] 
                if edge.sides[v] == match_color:
                    return piece, v, h
                elif edge.sides[h] == match_color:
                    return piece, h, v
        return None, None, None
    
    def _check_bot_edges(self, match_color):

        faces = ['front', 'left', 'back', 'right']

        for face in faces:
            edge = self.bot_layer[f'{face}_middle']
            if edge.sides[face] == match_color:
                return face
    
    
    def _check_bot_face(self, match_color):

        faces = ['front', 'left', 'back', 'right']

        for face in faces:
            edge = self.bot_layer[f'{face}_middle']
            if edge.sides['bottom'] == match_color:
                return face

    def _make_daisy(self):
        '''
        Bring 4 bottom color edge pieces to top layer, creating a daisy-like
        shape around that opposing center.
        '''
        # list the 4 edges, and solve them 1 at a time?
        # or keep looping the same logic until all 4 are done
        bottom_center = self.bot_layer['bottom_center'].sides['bottom']

        top_edges = [
            self.top_layer['front_middle'].sides,
            self.top_layer['left_middle'].sides,
            self.top_layer['right_middle'].sides,
            self.top_layer['back_middle'].sides,
        ]

        while not all(edge['top'] == bottom_center for edge in top_edges):

            # TOP LAYER MATCHERS
            # if the side face of a top edge matches, 
            # turn that face clockwise or counter,
            # turn the top the opposite way
            # turn the face it attached to the same opposite way

            # check top layer and return first instance of match or None

            face = self._check_top_edges(bottom_center)
            print("Face found:", face)
            while face is not None:
                if face == 'right':
                    print("right face")
                    self._R_prime()
                    self._U()
                    self._F_prime()
                elif face == 'front':
                    print("front face")
                    self._F_prime()
                    self._U()
                    self._L_prime()
                elif face == 'left':
                    print("left face")
                    self._L_prime()
                    self._U()
                    self._B_prime()
                elif face == 'back':
                    print("back face")
                    self._B_prime()
                    self._U()
                    self._R_prime()
                
                face = self._check_top_edges(bottom_center)
                print("Next face:", face)


            # MID LAYER MATCHERS
            # if a middle edge matches, rotate top until the wrong color
            # is above it and turn it up
            piece, side, face = self._check_mid_edges(bottom_center)
            while piece is not None:
                print("piece found:", piece)

                # if we know the 2 'directions' separately
                # reference the side its on by that direction
                # reference the place is going by the other direction + middle
                # locate the correct direction by joining them (always need [front, back] first)
                # first-pass: return 3 values from func
                while self.top_layer[f'{face}_middle'].sides['top'] == bottom_center:
                    print('turning top')
                    self._U()

                if piece == 'front_right':
                    if side == 'right':
                        print("its on the right")
                        self._F_prime()
                    elif side == 'front':
                        print("its on the front")
                        self._R()

                elif piece == 'front_left':
                    if side == 'left':
                        print("its on the left")
                        self._F()
                    elif side == 'front':
                        print("its on the front")
                        self._L_prime()
                
                elif piece == 'back_right':
                    if side == 'right':
                        print("its on the right")
                        self._B()
                    elif side == 'back':
                        print("its on the back")
                        self._R_prime()
                
                elif piece == 'back_left':
                    if side == 'left':
                        print("its on the left")
                        self._B_prime()
                    elif side == 'back':
                        print("its on the back")
                        self._L()


                piece, side, face = self._check_mid_edges(bottom_center)




            # BOT LAYER MATCHERS
            # if a bot layer edge matches,
            # rotate top until same face top edge isnt a match
            # rotate clockwise or counter
            # now treat like middle layer

            face = self._check_bot_edges(bottom_center)
            while face is not None:
                while self.top_layer[f'{face}_middle'].sides['top'] == bottom_center:
                    self._U()
                
                if face == 'front':
                    self._F()
                    self._U()
                    self._R()
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
            
                face = self._check_bot_edges(bottom_center)

            # The last remaining place for opposing edges is the bottom face
            # if the right color is on the bottom edge
            # we simply rotate the top until the corresponding side is is match free
            # the turn the piece up twice
            face = self._check_bot_face(bottom_center)
            while face is not None:

                while self.top_layer[f'{face}_middle'].sides['top'] == bottom_center:
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

                face = self._check_bot_face(bottom_center)

    def _bottom_cross(self):
        '''
        Move edge pieces from top to bottom, creating a cross shape in the 
        correct position on the bottom face.
        '''

        self._make_daisy()

        bottom_center = self.bot_layer['bottom_center'].sides['bottom']


        # while any of the top edges match the bottom
        # while any(edge.sides['top'] == bottom_center for edge in top_edges):
        # find one that matches
        for face in ['front', 'left', 'back', 'right']:

            center = self.mid_layer[f'{face}_center'].sides[face]
            top = self.top_layer[f'{face}_middle'].sides['top']
            print(self)


            while (self.top_layer[f'{face}_middle'].sides[face], top) != (center, bottom_center):
                self._U()
                top = self.top_layer[f'{face}_middle'].sides['top']
                print("center/top:", center, '/', self.top_layer[f'{face}_middle'].sides[face])
                print("top side of edge:", top, "-- should match", bottom_center)
                print("face", face)

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
        verticals = ['front', 'back']
        horizontals = ['left', 'right']

        for v in verticals:
            for h in horizontals:
                piece = f'{v}_{h}'
                sides = [self.top_layer[piece].sides[side] for side in self.top_layer[piece].sides if side != 'top']
                if match_color in sides:
                    return self.top_layer[piece]
        
        return None
    
    def _find_matching_center(self, match_color):
            for face in ['front', 'right', 'back', 'left']:
                if self.mid_layer[f'{face}_center'].sides[face] == match_color:
                    return face
        
    def _solve_bot_layer_trigger_helper(self, match_color):


        # when we find one, identify its partner color (the non-top one) 

        # rotate til partner matches center
        # determine side to do appropriate trigger <- this seems initially difficult
        pass

    def _solve_bot_layer_double_trigger_helper(self, match_color):

        self._solve_bot_layer_trigger_helper(match_color)
        pass
    
    def _solve_bot_layer(self):
        '''
        Solve the rest of the bottom layer, and in the process, the bottom
        face.
        '''

        self._bottom_cross()
        bottom_center = self.bot_layer['bottom_center'].sides['bottom']

        verticals = ['front', 'back']
        horizontals = ['left', 'right']
        # ALL CODE UNDER THIS NEEDS TO RUN INSIDE WHILE BOTTOM FACE NOT ALL THE SAME

        # find a piece that has match_color on it (not on top side)
        piece = self._check_top_corners(bottom_center)
        # find the color on the side thats not the match or the top
        while piece is not None:
            for side in piece.sides:
                if side != 'top' and piece.sides[side] != bottom_center:
                    other_color = piece.sides[side]
            # find which center is that color
            face = self._find_matching_center(other_color)
            
            # turn until it matches
            # track same face color to match, and side colors to match bottom 
            if face in horizontals:
                # face obvi needs to match
                # and then horizontal needs to match too 
                # good news is we know the piece we're matching
                while ((self.top_layer[f'front_{face}'].sides[face], self.top_layer[f'front_{face}'].sides['front']) != (other_color, bottom_center)
                and (self.top_layer[f'back_{face}'].sides[face], self.top_layer[f'back_{face}'].sides['back']) != (other_color, bottom_center)):
                    print("here")
                    self._U()

            elif face in verticals:
                while ((self.top_layer[f'{face}_right'].sides[face], self.top_layer[f'{face}_right'].sides['right']) != (other_color, bottom_center)
                and (self.top_layer[f'{face}_left'].sides[face], self.top_layer[f'{face}_left'].sides['left']) != (other_color, bottom_center)):
                    print("here")
                    self._U()
            # but it needs to be tracked together not independently
            # but also each side needs to be a separate pair





        # first check for top layer (non-top-side)
        # find the piece, and the side for the matching color
        # other side will be the face to align

        # the next step is to get the other color


        # problem = reference changes as you go. 
        # solution = maybe once we have the 'other' color, approach it from the center
        # for face in each of the possible faces
            # get the face that has the appropriate color
            # problem = how to know if it will be up to the right, or up to the left
            # solution = the face will be the common thing to match on
            
            # need to line up with correct center and know which side we are
        # rotate til it matches the center
        # trigger (based on center)
        # this needs to be exported to a function

        # if none on top layer, check top side
        # rotate until it does NOT match corresponding on bottom
        # double trigger
        # call check top layer function
        # this will also be exported
        self._solve_bot_layer_double_trigger_helper(bottom_center)
        # if none on top side, check bottom (non-bottom-side)
        # trigger up to top 
        # go back to step 2 
        
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

        self._bottom_cross()

        self._solve_bot_layer()

        self._solve_mid_layer()

        self._get_top_cross()

        self._solve_top_face()

        self._final_step()

