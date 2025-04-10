import pygame


class Food:
    __radius = -1
    __curr_pos = -1

    def __init__(self):
        self.set_radius(10)
        self.set_curr_pos(pygame.math.Vector2(50, 50))

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
