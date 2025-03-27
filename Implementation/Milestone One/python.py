# Best Group/Group Python
import pygame


class Python:
    # remember to create a getter and setter if you create a new var (and also to set it in __init__)
    __length = -1
    # pygame uses format K_DIRECTION, so that's what I'm using
    __curr_direction = "ERR"
    __curr_score = -1
    __head_pos = -1
    # This list will contain a list of vectors to draw from using pygame.math.Vector2()
    # (in hindsight a 3-dimensional list would've made more sense)
    __pos_list = [None]

    def __init__(self):
        self.set_length(1)
        self.set_curr_direction("right")
        self.set_curr_score(0)
        self.set_pos_list([pygame.math.Vector2(480, 360)])
        self.set_head_pos(pygame.math.Vector2(480, 360))

    # helpers
    def change_head_pos(self):
        print(self.get_curr_direction())
        match self.get_curr_direction():
            case "up":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y - 5))
            case "down":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y + 5))
            case "right":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x + 5, self.get_head_pos().y))
            case "left":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x - 5, self.get_head_pos().y))
        lst_change = self.get_pos_list()

        lst_change[0] = self.get_head_pos()
        self.set_pos_list(lst_change)


    # getters
    def get_length(self):
        return self.__length

    def get_curr_direction(self):
        return self.__curr_direction

    def get_curr_score(self):
        return self.__curr_score

    def get_pos_list(self):
        return self.__pos_list

    def get_head_pos(self):
        return self.__head_pos

    # setters
    def set_length(self, length):
        self.__length = length

    def set_curr_direction(self, direction):
        self.__curr_direction = direction

    def set_curr_score(self, score):
        self.__curr_score = score

    def set_pos_list(self, positions):
        self.__pos_list = positions

    def set_head_pos(self, head_position):
        self.__head_pos = head_position

    # __str__
    def __str__(self):
        tempstr = ("Length: " + str(self.get_length()) + "\nDirection: " + str(self.get_curr_direction()) +
                   "\n Score:" + str(self.get_curr_score()) + "\nPosition list: " + str(self.get_pos_list()))
        return tempstr
