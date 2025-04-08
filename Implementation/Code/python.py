# Best Group/Group Python
import pygame


class Python:
    # remember to create a getter and setter if you create a new var (and also to set it in __init__)
    __length = -1
    # pygame uses format K_DIRECTION, so that's what I'm using
    __curr_direction = "ERR"
    __curr_score = -1
    __previous_score = -1
    __head_pos = -1
    # This list will contain a list of vectors to draw from using pygame.math.Vector2(), which stores an x and y value
    # individual X or Y value can be called with [variable].x or [variable].y
    __pos_list = [None]
    __previous_position = None
    # initializes class once created
    __next_direction = "ERR"

    def __init__(self, previous_score):
        self.set_length(1)
        self.set_curr_direction("none")
        self.set_curr_score(0)
        self.set_pos_list([pygame.math.Vector2(480, 360), pygame.math.Vector2(500, 360)])
        self.set_head_pos(pygame.math.Vector2(480, 360))
        self.set_previous_score(previous_score)
        self.set_next_direction("none")
    # helpers

    # changes position of head depending on the state of __curr_direction
    def change_head_pos(self):
        # set curr direction to next direction
        self.set_curr_direction(self.get_next_direction())
        # stores previous position that is used for adding parts to the snakes body
        self.set_previous_position(pygame.math.Vector2(self.get_pos_list()[-1]))
        match self.get_curr_direction():
            case "up":
                self.change_body_position()
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y - 20))
            case "down":
                self.change_body_position()
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y + 20))

            case "right":
                self.change_body_position()
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x + 20, self.get_head_pos().y))

            case "left":
                self.change_body_position()
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x - 20, self.get_head_pos().y))

        # updates variable
        lst_change = self.get_pos_list()
        lst_change[0] = self.get_head_pos()
        self.set_pos_list(lst_change)

# changes position of body
    def change_body_position(self):
        new_pos_list = []
        # uses a reversed list to pass coordinates backwards
        for last_pos in reversed(range(1, len(self.get_pos_list()))):
            new_pos_list.append(pygame.math.Vector2(self.get_pos_list()[last_pos - 1]))
        new_pos_list.append(pygame.math.Vector2(self.get_pos_list()[0]))
        # list is re-reversed to use for movement
        # list must be reversed manually because slicing changes the data type of the list
        new_list_reversed = []
        for i in reversed(range(len(new_pos_list))):
            new_list_reversed.append(pygame.math.Vector2(new_pos_list[i]))
        self.set_pos_list(new_list_reversed)

    # handles size change
    def increase_size(self):
        # uses the stored position to create a body part for the snake
        new_pos_list = self.get_pos_list()
        new_pos_list.append(self.get_previous_position())
        self.set_pos_list(new_pos_list)
        self.set_length(self.get_length() + 1)

    # returns x coordinates of get_pos_list() this is used in apple_collision for forbidden coordinates
    def get_x_coordinates(self):
        x = []
        for length in self.get_pos_list():
            x.append(length.x)
        return x

    # same thing but for y
    def get_y_coordinates(self):
        y = []
        for length in self.get_pos_list():
            y.append(length.y)
        return y

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

    def get_previous_score(self):
        return self.__previous_score

    def get_previous_position(self):
        return self.__previous_position

    def get_next_direction(self):
        return self.__next_direction

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

    def set_previous_score(self, previous_score):
        self.__previous_score = previous_score

    def set_previous_position(self, previous_position):
        self.__previous_position = previous_position

    def set_next_direction(self, next_direction):
        self.__next_direction = next_direction

    # __str__
    def __str__(self):
        tempstr = ("Length: " + str(self.get_length()) + "\nDirection: " + str(self.get_curr_direction()) +
                   "\n Score:" + str(self.get_curr_score()) + "\nPosition list: " + str(self.get_pos_list()))
        return tempstr
