import random
from piece import Piece, Center, Edge, Corner

class RubiksCube:
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
        colors = ['w', 'y', 'o', 'b', 'r', 'g']
        # list all the center pieces
        centers = [self.bot_layer['bottom_center'],
                   self.mid_layer['right_center'],
                   self.mid_layer['left_center'],
                   self.mid_layer['front_center'],
                   self.mid_layer['back_center'],
                   self.top_layer['top_center']]

        # looping through center pieces
        for piece in centers:
            color = random.choice(colors)
            # assign it a random choice from the colors
            side = list(piece.sides.keys())[0]
            piece.sides[side] = color
            # remove that color from list
            colors.remove(color)

        self.opposing_colors.append(
            {self.bot_layer['bottom_center'].sides['bottom'], self.top_layer['top_center'].sides['top']}
            )
        self.opposing_colors.append(
            {self.mid_layer['right_center'].sides['right'], self.mid_layer['left_center'].sides['left']}
            )
        self.opposing_colors.append(
            {self.mid_layer['front_center'].sides['front'], self.mid_layer['back_center'].sides['back']}
            )

    def initialize_edges(self):
        # list of colors again
        colors = ['w', 'y', 'o', 'b', 'r', 'g']
        # dict to keep track of how many times each color has been used
        colors_count = {color: 0 for color in colors}
        # list of edges
        edges = [self.bot_layer['front_middle'],
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

        complete_edges = []
        # looping through edges
        for edge in edges:
            print('Colors:', colors)
            print('Colors Count:', colors_count)
            print("Complete Edges:", complete_edges)
            # random choice from colors list
            # make sure it's not been picked out already
            # maybe remove from colors list once picked out
            first_choice = random.choice(colors) 
            # assign to side1
            edge.side1 = first_choice

            # select another choice
            second_choice = random.choice(colors)
            # confirm its not the same or the opposing color
            while ((second_choice == first_choice)
            or ({first_choice, second_choice} in self.opposing_colors)
            or ({first_choice, second_choice} in complete_edges)):
                second_choice = random.choice(colors)
            # assign to second
            edge.side2 = second_choice
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
        pass

    def initialize_cube(self):
        self.initialize_centers()

        self.initialize_edges()

        self.initialize_corners()

