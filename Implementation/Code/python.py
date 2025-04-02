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
    # stores directions for body
    __body_directions = [None]

    # initializes class once created
    def __init__(self):
        self.set_length(1)
        self.set_curr_direction("none")
        self.set_curr_score(0)
        self.set_pos_list([pygame.math.Vector2(480, 360)])
        self.set_head_pos(pygame.math.Vector2(480, 360))
        self.set_previous_score(0)

    # helpers

    # changes position of head depending on the state of __curr_direction
    def change_head_pos(self):
        print(self.get_curr_direction())
        match self.get_curr_direction():
            case "up":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y - 20))
                self.body_directions("up")
            case "down":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x, self.get_head_pos().y + 20))
                self.body_directions("down")
            case "right":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x + 20, self.get_head_pos().y))
                self.body_directions("right")
            case "left":
                self.set_head_pos(pygame.math.Vector2(self.get_head_pos().x - 20, self.get_head_pos().y))
                self.body_directions("left")
        # updates variable
        lst_change = self.get_pos_list()
        lst_change[0] = self.get_head_pos()
        self.set_pos_list(lst_change)
    # not ready to test, still need to make move and add parts when apple is collected

    def body_directions(self, direction):
        new_lst = []
        for previous_dir in reversed(range(len(self.get_body_direction()))):
            new_lst.append(self.get_body_direction()[previous_dir - 1])
        new_lst.append(direction)
        new_lst = new_lst.reverse()

    # handles size change
    def increase_size(self):
        # this appends the direction of the last body part to the new body part, this will cause a weird interation if
        # the last part is in a corner, but it will be functional as long as border collision does not apply to the body
        # which it has no reason to
        self.set_body_directions([self.get_body_direction(), self.get_body_direction()[self.get_length]])
        # match case functions similarly to an if statement, is usually more efficient and makes sense here since
        # we know the possible output
        match self.get_body_direction()[self.get_length]:
            # this is formatted as set_pos_list([get_pos_list(),
            # vector(poslist[last].x +- change, vector(poslist[last].y += change)])
            # change is in the opposite direct of where its currently heading
            case "up":
                self.set_pos_list([self.get_pos_list(),
                                   pygame.math.Vector2(self.get_pos_list()[self.get_length()].x,
                                                       self.get_pos_list()[self.get_length()].y - 20)])
            case "down":
                self.set_pos_list([self.get_pos_list(),
                                   pygame.math.Vector2(self.get_pos_list()[self.get_length()].x,
                                                       self.get_pos_list()[self.get_length()].y + 20)])
            case "right":
                self.set_pos_list([self.get_pos_list(),
                                   pygame.math.Vector2(self.get_pos_list()[self.get_length()].x - 20,
                                                       self.get_pos_list()[self.get_length()].y)])
            case "left":
                self.set_pos_list([self.get_pos_list(),
                                   pygame.math.Vector2(self.get_pos_list()[self.get_length()].x + 20,
                                                       self.get_pos_list()[self.get_length()].y)])
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

    def get_body_direction(self):
        return self.__body_directions

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

    def set_body_directions(self, directions):
        self.__body_directions = directions

    # __str__
    def __str__(self):
        tempstr = ("Length: " + str(self.get_length()) + "\nDirection: " + str(self.get_curr_direction()) +
                   "\n Score:" + str(self.get_curr_score()) + "\nPosition list: " + str(self.get_pos_list()))
        return tempstr
