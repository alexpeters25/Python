# Best Group/Group Python
# All code surrounding pygame heavily references pygame documentation
# Sprint 1: "Snake" that can be controlled by the player
import pygame
from python import Python


def main():
    running = True
    screen, clock, snake = initialize()

    while running:
        clock.tick(60)
        render(screen, snake)
        snake = key_input(snake)
        print(snake.get_curr_direction())
        snake.change_head_pos()
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
    return display, clock, snake


def render(screen, snake):
    rect_size = 50
    # This fills the background, so the previous image does not stay on screen
    screen.fill("white")

    # render snake here
    for length in range(len(snake.get_pos_list())):
        pygame.draw.rect(screen, "green", rect=(snake.get_pos_list()[length].x, snake.get_pos_list()[length].y,
                                                rect_size, rect_size))

    # renders display
    pygame.display.flip()



def key_input(snake):
    keys = pygame.key.get_pressed()
    # sets the direction the snake is currently headed, which changes position in main loop
    if keys[pygame.K_UP]:
        snake.set_curr_direction("up")

    elif keys[pygame.K_DOWN]:
        snake.set_curr_direction("down")

    elif keys[pygame.K_RIGHT]:
        snake.set_curr_direction("right")

    elif keys[pygame.K_LEFT]:
        snake.set_curr_direction("left")


    return snake



if __name__ == "__main__":
    main()
