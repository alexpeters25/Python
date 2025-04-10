# Best Group/Group Python
# All code surrounding pygame heavily references pygame documentation


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

    #### trying to import the picture of our dear leader (NOT mf'in WORKING)
    adams_snake_face = pygame.image.load("Images/french_face_real.png").convert_alpha()
    adams_snake_face = pygame.transform.scale(adams_snake_face, size=(65, 65))

    apple_image = pygame.image.load("Images/pixel_apple.png").convert_alpha()
    apple_image = pygame.transform.scale(apple_image, size=(35, 35))

    title_text = pygame.image.load("Images/python_text.png").convert_alpha()
    title_text = pygame.transform.scale(title_text, size=(349/2, 126/2))

    #### trying to import the song before the while running part
    # after time delay music starts
    pygame.mixer.music.load("Sounds/gameSong.wav")
    # play the music, args: how many times it repeats, where to start playing
    pygame.mixer.music.play(-1, 0.0)

    # This loop runs through different functions until the user closes the window
    while running:
        # when the game starts audio file of adam saying "hello everybowdy" plays

        # sets frame rate
        clock.tick(60)
        # calls render function to render screen
        render(screen, snake, food, adams_snake_face, apple_image, title_text)
     
        # border function set up where if the snake head touches it, the game quits running
        border(snake)
        if snake.get_curr_direction() == "stop":
            snake = Python(snake.get_curr_score())
        # take user input
        key_input(snake)

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
    snake = Python(0)
    display = pygame.display.set_mode(size=(720, 720))          # Adjust for window
    clock = pygame.time.Clock()
    food = Food()
    return display, clock, snake, food


def render(screen, snake, food, adams_snake_face, apple_image, title_text):
    # var for rectangle size
    rect_size = 20
    # var for food size, always proportional to rect_size
    food_size = rect_size / 2
    # list stores rectangles to check for collision
    snakes_squares = []
    # This fills the background, so the previous image does not stay on screen
    screen.fill(color=(76, 179, 252))

    # Screen dimensions currently 720x720
    x = 720
    y = 720
    # playing field

    face = adams_snake_face.get_rect(center=(50, 50))
    playing_field = pygame.Rect(60, 60, x-120, y-120)
    field_border = pygame.Rect(55, 55, x-110, y-110)
    pygame.draw.rect(screen, (0, 77, 134), rect=playing_field)
    pygame.draw.rect(screen, (46, 26, 10), rect=field_border, width=5)

    screen.blit(title_text, ((x/2)-(349/4), -1))

    # field grid
    # Create each darker square in grid
    grid_squares_light = []
    for length in range(15):
        for width in range(15):
            grid_squares_light.append(
                pygame.Rect(
                    60+(2*rect_size*width
                        ), 60+(2*rect_size*length
                               ), rect_size, rect_size
                )
            )
            grid_squares_light.append(
                pygame.Rect(
                    (60 + rect_size
                     ) + 2*rect_size*width,
                    (60+rect_size)+(2*rect_size*length
                                    ), rect_size, rect_size
                )
            )

    # Print each square onto the field
    for i in range(len(grid_squares_light)):
        pygame.draw.rect(
            screen, (
                0, 67, 124), rect=(
                grid_squares_light[i]
            )
        )

    # update score
    pygame.display.set_caption("Score: " + str(snake.get_curr_score()) + " | Previous Score: " +
                               str(snake.get_previous_score()))
    # render snake here
    for width in range(len(snake.get_pos_list())):
        # uses draw.rect() which is formatted  as (display being drawn on, color,
        #                                         rect(x position, y position, width, length)

        snakes_squares.append(
            pygame.Rect(
                snake.get_pos_list()[width].x, snake.get_pos_list()[width].y,
                                          rect_size, rect_size
            )

        )

        pygame.draw.rect(
            screen, color=(206, 137, 0), rect=(
                snakes_squares[width]
            )
        )

    apple = pygame.draw.circle(
        screen, (185, 0, 0), (
            food.get_curr_pos().x, food.get_curr_pos().y
        ), food_size
    )
    apple_collision(
        snakes_squares, apple, snake, food
    )
    snake_collision(snakes_squares, snake)

    # DMRE1 helped us get this right after 3 hours of failure (ChatGPT)
    head_centered = adams_snake_face.get_rect(center=(
        snake.get_pos_list()[0].x + 10,
        snake.get_pos_list()[0].y + 10
    ))

    screen.blit(adams_snake_face, head_centered)

    apple_centered = apple_image.get_rect(center=food.get_curr_pos())
    screen.blit(apple_image, apple_centered)


# renders display, end of function

    pygame.display.flip()
    pygame.display.update()


def key_input(snake):
    # this creates a list of booleans depending on what keys are being pressed
    keys = pygame.key.get_pressed()
    # check keys being pressed, and changes current direction depending on the key being pressed
    # pygame.K_CHARACTER references the point in the list referencing that character

    if (keys[pygame.K_UP] or keys[pygame.K_w]) and snake.get_curr_direction() != "down":
        snake.set_next_direction("up")

    elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and snake.get_curr_direction() != "up":
        snake.set_next_direction("down")

    elif ((keys[pygame.K_RIGHT] or keys[pygame.K_d]) and snake.get_curr_direction() != "left" and
          snake.get_curr_direction() != "none"):
        snake.set_next_direction("right")

    # this 'or' is causing problems
    elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and snake.get_curr_direction() != "right":
        snake.set_next_direction("left")


def apple_collision(snake_rects, apple_circle, snake, food):
    if snake_rects[0].collidepoint(food.get_curr_pos()):
        # this is where to add the sfx upon collision

        snake.increase_size()
        forbidden_x = snake.get_x_coordinates()
        forbidden_y = snake.get_y_coordinates()
        snake.set_curr_score(snake.get_curr_score() + 1)
        food.position_change(forbidden_x, forbidden_y)
        # this will also update snake length later


def snake_collision(snake_rects, snake):
    for index in range(1, len(snake_rects)):
        if snake_rects[0].collidepoint(snake.get_pos_list()[index]):
            snake.set_curr_direction("stop")


def border(snake):
    if snake.get_pos_list()[0][0] <= 59 or snake.get_pos_list()[0][0] >= 641:
        snake.set_curr_direction("stop")
    elif snake.get_pos_list()[0][1] <= 59 or snake.get_pos_list()[0][1] >= 641:
        snake.set_curr_direction("stop")

    return snake


if __name__ == "__main__":
    main()
