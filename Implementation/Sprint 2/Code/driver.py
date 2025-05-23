# Best Group/Group Python
# All code surrounding pygame heavily references pygame documentation
# Sprint 1: "Snake" that can be controlled by the player
import pygame
import time
from python import Python
from food import Food


def main():
    running = True
    # initializes pygame, a clock (for frame rate/anything else we might need it for later, and the snake object
    screen, clock, snake, food = initialize()
    # used to ensure movement only occurs every 100 ms (subject to change)
    movement_timer = time.time()

    # This loop runs through different functions until the user closes the window
    while running:
        # sets frame rate
        clock.tick(60)
        # calls render function to render screen
        render(screen, snake, food)
        # checks input
        snake = key_input(snake)
        # border function set up where if the snake head touches it, the game quits running
        border(snake)
        if snake.get_curr_direction() == "stop":
            running = False
        # calls the function from the python class that changes the position of the snakes head
        # if statement triggers every 100 ms and resets timer
        if movement_timer - time.time() < -0.1:
            snake.change_head_pos()
            movement_timer = time.time()
        # Allows "X" button on window to be pressed

        # Need a coordinate system so that fruit placement can be randomized
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    return


# initializes pygame: referenced https://www.pygame.org/docs/, also referenced for rendering
def initialize():
    pygame.init()
    snake = Python()
    display = pygame.display.set_mode(size=(960, 720))
    clock = pygame.time.Clock()
    food = Food()
    return display, clock, snake, food


def render(screen, snake, food):
    # var for rectangle size
    rect_size = 20
    food_size = 15

    # This fills the background, so the previous image does not stay on screen
    screen.fill("white")

    # render snake here
    for length in range(len(snake.get_pos_list())):
        # uses draw.rect() which is formatted  as (display being drawn on, color,
        #                                         rect(x position, y position, width, length)
        pygame.draw.rect(screen, "green", rect=(snake.get_pos_list()[length].x, snake.get_pos_list()[length].y,
                                                rect_size, rect_size))

    pygame.draw.circle(screen, "red", (food.get_curr_pos().x, food.get_curr_pos().y), food_size)
    # renders display, end of function
    pygame.display.flip()


def key_input(snake):
    # this creates a list of booleans depending on what keys are being pressed
    keys = pygame.key.get_pressed()
    # check keys being pressed, and changes current direction depending on the key being pressed
    # pygame.K_CHARACTER references the point in the list referencing that character
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        snake.set_curr_direction("up")

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        snake.set_curr_direction("down")

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        snake.set_curr_direction("right")

    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        snake.set_curr_direction("left")

    return snake


def border(snake):
    if snake.get_pos_list()[0][0] <= 10 or snake.get_pos_list()[0][0] >= 910:
        snake.set_curr_direction("stop")
    elif snake.get_pos_list()[0][1] <= 10 or snake.get_pos_list()[0][1] >= 660:
        snake.set_curr_direction("stop")

    return snake

# Need a function to generate the head?
'''
def adam_head():
    # head = pygame.image.load("spanieram.jpg").convert_alpha()
'''

if __name__ == "__main__":
    main()
