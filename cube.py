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
                        self.bot_layer['back_left'],
                        self.bot_layer['back_right'],
                        self.top_layer['front_left'],
                        self.top_layer['front_left'], 
                        self.top_layer['front_left'],
                        self.top_layer['front_left']]
        
        self.opposing_colors = []
    
    def __repr__(self):
        return f"""RubiksCube({self.top_layer}, {self.mid_layer}, {self.bot_layer})"""

    def __str__(self):
        output = f"""
        Top layer: {self.top_layer}\n\n\n
        Middle layer: {self.mid_layer}\n\n\n
        Bottom layer: {self.bot_layer}\n\n\n"""
        return output

    def initialize_centers(self):
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

    def initialize_edges(self):
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

    def initialize_corners(self):
        colors = RubiksCube.colors.copy()
        colors_count = {color: 0 for color in colors}

        color_pairs = []
        for color1 in colors:
            for color2 in colors:
                if color1 != color2 and (color1, color2) not in self.opposing_colors:
                    color_pairs.append((color1, color2))
        color_pairs_count = {color_pair: 0 for color_pair in color_pairs}
        print("Color pairs: ", color_pairs)
        
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
            
            print("Made it through second choice")
            print("Colors left", colors)

            # choose third color from 2 colors adjacent to second color
            # Logic: once we've chosen 2 colors, the third color can onlybe one of two
            # Pick one of those - make sure not to repick by A adding piece to complete
            # B increment count of colors, C check second_choice that we're not picking
            # a two-color combo that's been picked twice already
            third_choice = random.choice(colors)
            while (third_choice == first_choice or third_choice == second_choice
            or (first_choice, third_choice) in self.opposing_colors
            or (second_choice, third_choice) in self.opposing_colors
            or {first_choice, second_choice, third_choice} in complete_corners):
                third_choice = random.choice(colors)
            
            # assign it
            corner.sides[side3] = third_choice

            print("Made it through 3rd choice.")
            
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
                colors.remove(first_choice)
            if colors_count[third_choice] == 4:
                colors.remove(first_choice)


    def initialize_cube(self):
        self.initialize_centers()

        self.initialize_edges()

        self.initialize_corners()

