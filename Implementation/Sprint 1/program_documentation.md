# Program documentation
## Added this milestone
### Objects
- [Python](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Code/python.py)
  - this object is used to control the snake
  - variables:
    - __curr_direction: stores current direction as a string
    - __curr_score: stores current score of the snake, unused in this iteration
    - __head_pos = used to store the position of the head
    - __pos_list = to be used to store coordinates of all snake parts
  - functions:
    - setters
    - getters
    - [change_head_pos()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Images/change_pos_s1.png)
      - this function changes the head position accordingly depending on the state of __curr_direction
      
### Driver
- [driver.py](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Code/driver.py)
  - [initialize()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Images/initialize_s1.png)
    - initializes pygame
    - initiallizes the snake using the class in Python.py
    - initializes the window display
    - initializes pygame.time.Clock to track framerate
    - returns all of the above
  - [render()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Images/render_s1.png)
    - accepts variables for the display and the snake
    - draws the snake using draw.rect from the pygame library in conjunction with the position variables from the Python class
    - fills screen with white to prevent game from drawing over itself
    - usees pygame.display.flip() to render screen
  - [key_input()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Images/key_input_s1.png)
    - accepts variables from the Python class
    - checks the currently pressed keys using pygame.key.get_pressed, then changes the curr_direction variable within the snake class accordingly
  - [main()](https://github.com/alexpeters25/Python/blob/main/Implementation/Sprint%201/Images/main_s1.png)
    - creates a variable to control a while loop
    - creates variables used for the screen, clock, and snake by calling initialize()
    - begins a while loop
      - sets framerate to 60
      - calls render() and feeds the screen and snake variables
      - calls changte_head_pos from the Python class
      - begins a for loop that checks if the "X" button on the window has been pressed
