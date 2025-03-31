import pygame
import random


class Food:
    __radius = -1
    __curr_pos = -1

    def __init__(self):
        self.set_radius(10)
        self.position_change()

    # helpers
    def position_change(self):
        # this checks the screen size, so we don't have to change this later
        screen_size = str(pygame.display.get_surface())
        screen_size = screen_size.strip('<Surface(')
        screen_size = screen_size.strip("SW)>")
        screen_size_lst = screen_size.split("x")
        rand_position_x = random.randrange(start=0, stop=int(screen_size_lst[0]), step=20)
        rand_position_y = random.randrange(start=0, stop=int(screen_size_lst[1]), step=20)
        self.set_curr_pos(pygame.math.Vector2(rand_position_x, rand_position_y))


    # getters
    def get_radius(self):
        return self.__radius

    def get_curr_pos(self):
        return self.__curr_pos

    # setters
    def set_radius(self, radius):
        self.__radius = radius

    def set_curr_pos(self, pos):
        self.__curr_pos = pos

    # toString
    def __str__(self):
        tempStr = ("Radius: " + str(self.get_radius()) + "\n" + "Position: " + str(self.get_curr_pos()))
        return tempStr
